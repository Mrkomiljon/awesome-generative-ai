#!/usr/bin/env python3
"""
GitHub Stars Auto-Updater

Updates markdown table rows that have a "Stars" column and a GitHub repository link.
"""

import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests


RATE_LIMIT_DELAY = 1.0
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")
HEADERS = {"Accept": "application/vnd.github+json"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"

REPO_URL_RE = re.compile(r"https://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
STAR_VALUE_RE = re.compile(r"^\d{1,3}(?:,\d{3})*$")
TABLE_DIVIDER_RE = re.compile(r"^:?-+:?$")


def get_github_stars(repo_url: str):
    match = REPO_URL_RE.search(repo_url)
    if not match:
        return None

    owner, repo = match.group(1), match.group(2)
    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    try:
        response = requests.get(api_url, headers=HEADERS, timeout=20)
    except requests.RequestException as exc:
        print(f"request failed for {owner}/{repo}: {exc}")
        return None

    if response.status_code == 200:
        return response.json().get("stargazers_count")
    if response.status_code == 404:
        print(f"repository not found: {owner}/{repo}")
        return None
    if response.status_code == 403:
        print(f"rate/auth issue for {owner}/{repo} (403)")
        return None

    print(f"http {response.status_code} for {owner}/{repo}")
    return None


def parse_table_row(line: str):
    stripped = line.strip()
    if not (stripped.startswith("|") and stripped.endswith("|")):
        return None
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def is_table_divider(cells):
    return all(TABLE_DIVIDER_RE.match(cell.replace(" ", "")) for cell in cells)


def rebuild_table_row(cells):
    return "| " + " | ".join(cells) + " |"


def find_repo_url(line: str):
    match = REPO_URL_RE.search(line)
    if not match:
        return None
    return f"https://github.com/{match.group(1)}/{match.group(2)}"


def update_file_stars(path: Path, cache: dict):
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    changed = False
    stars_col_index = None
    updated_rows = 0

    for i, line in enumerate(lines):
        cells = parse_table_row(line)
        if cells is None:
            if line.strip() == "":
                stars_col_index = None
            continue

        if "Stars" in cells:
            stars_col_index = cells.index("Stars")
            continue

        if is_table_divider(cells):
            continue

        if stars_col_index is None or stars_col_index >= len(cells):
            continue

        repo_url = find_repo_url(line)
        if not repo_url:
            continue

        if repo_url not in cache:
            cache[repo_url] = get_github_stars(repo_url)
            time.sleep(RATE_LIMIT_DELAY)

        stars = cache[repo_url]
        if stars is None:
            continue

        current = cells[stars_col_index].strip()
        if current == "-" or STAR_VALUE_RE.match(current):
            new_value = f"{stars:,}"
            if current != new_value:
                cells[stars_col_index] = new_value
                lines[i] = rebuild_table_row(cells)
                updated_rows += 1
                changed = True

    if changed:
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"updated {updated_rows} rows in {path.name}")
    else:
        print(f"no changes in {path.name}")

    return changed


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    print(f"star updater started at {now}")

    files = sorted(Path(".").glob("*.md"))
    cache = {}
    changed_files = []

    for path in files:
        if update_file_stars(path, cache):
            changed_files.append(path.name)

    if changed_files:
        print("updated files:", ", ".join(changed_files))
    else:
        print("no files changed")


if __name__ == "__main__":
    main()
