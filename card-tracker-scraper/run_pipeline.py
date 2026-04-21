from __future__ import annotations

import os

from dotenv import load_dotenv

from database.supabase_client import SupabaseStore
from enrichment.gemini_enricher import GeminiEnricher
from scrapers.cardmarket_scraper import CardMarketScraper
from scrapers.ebay_scraper import EbayScraper
from scrapers.psa_scraper import PsaScraper
from scrapers.tcgplayer_scraper import TcgPlayerScraper
from utils.helpers import RateLimiter, deduplicate


def parse_targets() -> list[str]:
    raw = os.getenv("PIPELINE_TARGETS", "pokemon")
    return [target.strip() for target in raw.split(",") if target.strip()]


def main() -> None:
    load_dotenv()

    targets = parse_targets()
    scrapers = [EbayScraper(), TcgPlayerScraper(), CardMarketScraper(), PsaScraper()]
    limiter = RateLimiter(delay_seconds=0.3)
    enricher = GeminiEnricher()
    store = SupabaseStore()

    all_listings = []
    snapshots = []

    for card_name in targets:
        for scraper in scrapers:
            listings = scraper.fetch(card_name)
            unique = deduplicate(listings)
            all_listings.extend(unique)
            snapshots.append(enricher.enrich(scraper.source, card_name, unique))
            limiter.wait()

    store.upsert_listings(all_listings)
    store.upsert_snapshots(snapshots)

    print(f"Saved {len(all_listings)} listings and {len(snapshots)} snapshots")


if __name__ == "__main__":
    main()
