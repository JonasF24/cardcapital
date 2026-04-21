# Deployment Guide

## 1) Prerequisites
- Python 3.11+
- GitHub repository
- Supabase project
- Gemini API key

## 2) Local bootstrap
```bash
cd card-tracker-scraper
cp .env.example .env
pip install -r requirements.txt
python run_pipeline.py
```

## 3) Database tables
Create two tables in Supabase:
- `market_listings`
- `market_snapshots`

Use JSON-compatible columns for payload fields or create typed columns matching the pydantic models in `utils/models.py`.

## 4) GitHub Actions secrets
Set these repository secrets:
- `GEMINI_API_KEY`
- `SUPABASE_URL`
- `SUPABASE_KEY`
- `EBAY_APP_ID`
- `TCGPLAYER_PUBLIC_KEY`
- `TCGPLAYER_PRIVATE_KEY`
- `CARDMARKET_APP_TOKEN`

## 5) Enable automation
Push to default branch. The workflow in `.github/workflows/daily-scrape.yml` runs daily at 02:00 UTC.
