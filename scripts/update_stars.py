#!/usr/bin/env python3
"""
GitHub Stars Auto-Updater
This script automatically updates GitHub star counts in README.md and ai-agents.md files.
"""

import re
import requests
import time
import os
from datetime import datetime

# GitHub API rate limiting
RATE_LIMIT_DELAY = 1  # seconds
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')

def get_github_stars(repo_url):
    """Fetch the star count from a GitHub repository"""
    try:
        # Convert "https://github.com/user/repo" → "user/repo"
        if 'github.com' in repo_url:
            repo_path = repo_url.split('github.com/')[-1].rstrip('/')
        else:
            return None

        api_url = f"https://api.github.com/repos/{repo_path}"
        headers = {}
        if GITHUB_TOKEN:
            headers['Authorization'] = f'token {GITHUB_TOKEN}'

        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data.get('stargazers_count', 0)
        elif response.status_code == 404:
            print(f"❌ Repository not found: {repo_path}")
            return None
        elif response.status_code == 403:
            print(f"⚠️ Rate limit exceeded for: {repo_path}")
            return None
        else:
            print(f"⚠️ Error {response.status_code} for: {repo_path}")
            return None

    except Exception as e:
        print(f"❌ Error fetching stars for {repo_url}: {e}")
        return None

def update_file_stars(file_path):
    """Update GitHub star counts in the specified file"""
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    print(f"🔄 Updating {file_path}...")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Find GitHub repo URLs in markdown links like [Repo](https://github.com/user/repo)
    repo_pattern = r'

\[(?:Repo|Website)\]

\((https://github\.com/[^/]+/[^/]+)\)'
    repos = re.findall(repo_pattern, content)

    updated_count = 0

    for repo_url in repos:
        print(f"🔍 Checking: {repo_url}")

        stars = get_github_stars(repo_url)
        if stars is not None:
            repo_name = repo_url.split('/')[-1]
            new_stars = f"{stars:,}"

            # Match table rows like | **RepoName** | 123,456 |
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if repo_name in line and '|' in line and any(char.isdigit() for char in line):
                    new_line = re.sub(r'\d+[,\d]*', new_stars, line)
                    if new_line != line:
                        lines[i] = new_line
                        updated_count += 1
                        print(f"✅ Updated {repo_name}: {new_stars} stars")
                        break

            content = '\n'.join(lines)

        time.sleep(RATE_LIMIT_DELAY)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✅ Updated {updated_count} repositories in {file_path}")
        return True
    else:
        print(f"ℹ️ No updates needed for {file_path}")
        return False

def main():
    """Main function"""
    print("🚀 Starting GitHub Stars Auto-Updater")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    files_to_update = [
        'README.md',
        'ai-agents.md'
    ]

    updated_files = []

    for file_path in files_to_update:
        if update_file_stars(file_path):
            updated_files.append(file_path)

    if updated_files:
        print(f"🎉 Successfully updated {len(updated_files)} files: {', '.join(updated_files)}")
    else:
        print("ℹ️ No files were updated")

    print("✅ GitHub Stars Auto-Updater completed")

if __name__ == "__main__":
    main()
