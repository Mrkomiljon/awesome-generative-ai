#!/usr/bin/env python3
"""
GitHub Stars Auto-Updater (fixed)
- Finds GitHub repo URLs in markdown files and updates numeric star counts in nearby table cells.
- Uses GITHUB_TOKEN from env (workflow should provide it).
"""

import re
import requests
import time
import os
from datetime import datetime

RATE_LIMIT_DELAY = 1  # seconds between API calls
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "")

HEADERS = {"Accept": "application/vnd.github.v3+json"}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"


def get_github_stars(repo_url):
    try:
        if "github.com" in repo_url:
            repo_path = repo_url.split("github.com/")[-1].rstrip("/")
        else:
            return None

        api_url = f"https://api.github.com/repos/{repo_path}"
        resp = requests.get(api_url, headers=HEADERS, timeout=15)

        if resp.status_code == 200:
            return resp.json().get("stargazers_count", 0)
        elif resp.status_code == 404:
            print(f"❌ Repository not found: {repo_path}")
            return None
        elif resp.status_code == 403:
            print(f"⚠️ Rate limit or auth error for: {repo_path} (status 403)")
            if "X-RateLimit-Remaining" in resp.headers:
                print("Rate limit remaining:", resp.headers.get("X-RateLimit-Remaining"))
            return None
        else:
            print(f"⚠️ HTTP {resp.status_code} for: {repo_path}")
            return None
    except Exception as e:
        print(f"❌ Error fetching {repo_url}: {e}")
        return None


def find_repo_urls(text):
    # find any GitHub repo URL in parentheses or plain text
    pattern = r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+"
    return list(dict.fromkeys(re.findall(pattern, text)))


def replace_star_counts_in_lines(lines, repo_url, new_stars):
    repo_name = repo_url.rstrip("/").split("/")[-1]
    updated = 0
    for i, line in enumerate(lines):
        if repo_name in line and "|" in line:
            # replace the first number-like group in the line (e.g., '12,345')
            new_line = re.sub(r"\d{1,3}(?:,\d{3})*", new_stars, line, count=1)
            if new_line != line:
                lines[i] = new_line
                updated += 1
                print(f"✅ Updated line for {repo_name}: {new_stars}")
                break
    return updated


def update_file_stars(path):
    if not os.path.exists(path):
        print(f"❌ File not found: {path}")
        return False

    print(f"🔄 Updating {path}...")
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    repos = find_repo_urls(content)
    if not repos:
        print("ℹ️ No GitHub repo URLs found in file")
        return False

    lines = content.splitlines()
    total_updated = 0

    for repo in repos:
        print(f"🔍 Checking {repo}")
        stars = get_github_stars(repo)
        if stars is None:
            print(f"⚠️ Skipping {repo}")
            time.sleep(RATE_LIMIT_DELAY)
            continue

        new_stars = f"{stars:,}"
        updated = replace_star_counts_in_lines(lines, repo, new_stars)
        total_updated += updated
        time.sleep(RATE_LIMIT_DELAY)

    if total_updated > 0:
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
        print(f"🎉 Updated {total_updated} entries in {path}")
        return True
    else:
        print("ℹ️ No numeric entries updated")
        return False


def main():
    print("🚀 GitHub Stars Auto-Updater (fixed)")
    print("⏰", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"))

    files = ["README.md", "ai-agents.md"]
    updated_any = False
    for p in files:
        if update_file_stars(p):
            updated_any = True

    if updated_any:
        print("✅ Done: some files updated")
    else:
        print("ℹ️ Done: no changes")

if __name__ == '__main__':
    main()
