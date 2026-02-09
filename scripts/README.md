# GitHub Stars Auto-Updater

This folder contains the single updater script used by GitHub Actions to refresh star counts.

## Files

- `update_stars_fixed.py`: updates markdown table rows that have both:
  - a `Stars` column
  - a GitHub repository link in the same row

## How It Works

1. Workflow runs daily (UTC) or manually.
2. Script scans top-level `*.md` files.
3. For rows in markdown tables, it detects the `Stars` column index.
4. It fetches stars from GitHub API.
5. It only updates valid star cells (`-` or numeric values).

## Why This Is Safe

- It does not replace arbitrary numbers in a line.
- It only edits rows with a recognized `Stars` column.
- It caches API results per repository URL.

## Local Run

```bash
python scripts/update_stars_fixed.py
```

Set `GITHUB_TOKEN` for higher API limits:

```bash
export GITHUB_TOKEN=your_token
python scripts/update_stars_fixed.py
```
