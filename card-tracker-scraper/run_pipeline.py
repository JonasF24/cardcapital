from __future__ import annotations

import logging
import os

from dotenv import load_dotenv

from database.supabase_client import SupabaseStore
from enrichment.gemini_enricher import GeminiEnricher
from scrapers.cardmarket_scraper import CardMarketScraper
from scrapers.ebay_scraper import EbayScraper
from scrapers.psa_scraper import PSAScraper
from scrapers.tcgplayer_scraper import TCGPlayerScraper
from utils.helpers import RateLimiter, deduplicate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_targets() -> list[str]:
    raw = os.getenv("PIPELINE_TARGETS", "pokemon")
    return [target.strip() for target in raw.split(",") if target.strip()]


def main() -> None:
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path=dotenv_path)

    targets = parse_targets()
    scrapers = [EbayScraper(), TCGPlayerScraper(), CardMarketScraper(), PSAScraper()]
    limiter = RateLimiter(delay_seconds=0.3)
    enricher = GeminiEnricher()
    store = SupabaseStore()

    all_listings = []
    snapshots = []

    for card_name in targets:
        for scraper in scrapers:
            try:
                listings = scraper.fetch(card_name)
                unique = deduplicate(listings)
                all_listings.extend(unique)
                snapshots.append(enricher.enrich(scraper.source, card_name, unique))
            except Exception:
                logger.exception(
                    "Scraper %s failed for card %r; skipping.", scraper.source, card_name
                )
            limiter.wait()

    store.upsert_listings(all_listings)
    store.upsert_snapshots(snapshots)

    if store.client:
        print(f"Saved {len(all_listings)} listings and {len(snapshots)} snapshots")
    else:
        print(
            f"Collected {len(all_listings)} listings and {len(snapshots)} snapshots"
            " (persistence skipped: Supabase not configured)"
        )


if __name__ == "__main__":
    main()
