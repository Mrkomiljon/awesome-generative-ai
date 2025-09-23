# 🤖 GitHub Stars Auto-Updater

This folder contains scripts for automatically updating GitHub repository star counts across all markdown files.

## 📁 Files

- `update_stars.py` - Main script that fetches star counts from GitHub API and updates files
- `README.md` - This file (description)

## 🔧 How It Works

1. **GitHub Actions** runs daily at UTC 00:00
2. **Python script** finds all GitHub repositories
3. **GitHub API** fetches real-time star counts
4. **All .md files** are updated with latest star counts
5. **Git commit** saves all changes automatically

## ⚙️ Configuration

- **Rate Limiting**: 1 second between each API request
- **GitHub Token**: Automatic (in GitHub Actions)
- **Update Schedule**: Daily at UTC 00:00
- **Manual Trigger**: Available via "workflow_dispatch" in GitHub Actions

## 🚀 Manual Execution

```bash
# Run locally
python scripts/update_stars.py

# Run via GitHub Actions
# GitHub repository -> Actions -> Update GitHub Stars -> Run workflow
```

## 📊 Results

The script updates the following files:

- `README.md` - Main repository file
- `ai-agents.md` - AI agents collection
- `talking-head.md` - Talking head papers & models
- `genai-apis.md` - Generative AI APIs
- `transformers.md` - Transformer models
- `stt-models.md` - Speech-to-text models
- `tts.md` - Text-to-speech models
- `voice-cloning.md` - Voice cloning models
- `text-to-image.md` - Text-to-image models
- `emotion-recognition.md` - Emotion recognition models
- `mcp.md` - Model Context Protocol servers
- `more_detailed.md` - Extended collection

**All GitHub star counts are updated in real-time across all files!**

## 🔄 Features

- **Automatic Updates**: Runs daily without manual intervention
- **Comprehensive Coverage**: Updates all .md files in the repository
- **Error Handling**: Continues working even if some repositories fail
- **Rate Limiting**: Respects GitHub API limits
- **Real-time Data**: Always shows current star counts
- **Git Integration**: Automatically commits and pushes changes

## 🛠️ Technical Details

- **Language**: Python 3.9+
- **Dependencies**: requests, beautifulsoup4
- **API**: GitHub REST API v3
- **Rate Limit**: 5000 requests/hour (with token)
- **File Types**: All .md files in repository
- **Pattern Matching**: `[Repo](https://github.com/user/repo)` format

## 📈 Statistics

- **200+ AI Agent Projects** tracked
- **1M+ Total Stars** across all repositories
- **Daily Updates** for all projects
- **Zero Manual Work** required