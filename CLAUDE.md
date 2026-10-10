# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A curated "awesome list" of generative AI resources. Almost all content is Markdown; the only code is a GitHub star-count updater. Most changes are adding a single entry to the right `docs/*.md` file (typical commit: "Add <Project> to <section>").

## Layout

- `README.md` — landing page and navigation hub (Start Here, Top Picks, Build Paths, Resource Index). Links into `docs/`. If you add a new `docs/` file, link it from the README's Resource Index (and Build Paths if relevant) and from `CONTRIBUTING.md`'s "Where to Add".
- `docs/*.md` — one file per topic (agents, MCP, STT/TTS, voice cloning, emotion recognition, text-to-image, talking head, transformers, GenAI APIs, context engineering). `docs/more_detailed.md` is the catch-all for broad references.
- `scripts/update_stars_fixed.py` — the star updater actually used by CI. `scripts/update_stars.py` and `test_update.py` (which invokes the old script) are legacy.
- `.github/workflows/update-stars.yml` — runs the updater daily at 02:00 UTC (and on manual dispatch) and auto-commits changes to `README.md` and `docs/*.md`.

## Adding entries (from CONTRIBUTING.md)

- Pick the correct file and section; match the surrounding table/bullet format exactly (column count and order vary per table).
- Official links first (GitHub repo, paper, project page, docs). Open-source or freely accessible resources.
- Descriptions: concise and factual, ~8–15 words, no promotional wording. Prefer ASCII.
- Check for duplicates before adding (grep the project name/URL across `README.md` and `docs/`).
- Formats:
  - Table row: `| **Project** | - | Short factual description | [Repo](https://github.com/org/repo) |`
  - Bullet: `- [Project](https://github.com/org/repo) - Short factual description`

## Star counts

Tables with a `Stars` header column get their star cells refreshed automatically. The updater only touches a row if it is in a table whose header contains a cell exactly `Stars`, the row contains a `https://github.com/owner/repo` link, and the current cell is `-` or a comma-formatted number. So when adding a row to such a table, put `-` in the Stars cell (CI fills it in) and include the GitHub link in the row. Don't hand-edit star numbers.

Run locally (needs `requests`; `GITHUB_TOKEN` raises the rate limit):

```bash
pip install requests
GITHUB_TOKEN=... python scripts/update_stars_fixed.py
```

The script rewrites table rows it updates (normalizing their cell spacing), so expect formatting diffs on touched rows. There is no lint or test suite.
