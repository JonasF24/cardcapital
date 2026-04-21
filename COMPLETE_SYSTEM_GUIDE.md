# Complete System Guide

This repository now includes:
1. `card-tracker-dashboard.html` and `CardTracker.jsx` for frontend visualization.
2. `card-tracker-scraper/` for backend ingestion, enrichment, and persistence.

## Integration flow
1. Pipeline scrapes sources daily.
2. Enrichment computes sentiment and score.
3. Snapshots are persisted to Supabase.
4. Frontend queries Supabase or a small API layer to render latest metrics.

## Suggested next step
Add a lightweight API endpoint (FastAPI/Next.js API route) that returns the latest `market_snapshots` and historic series for charts.
