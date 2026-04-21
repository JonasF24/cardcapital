from __future__ import annotations

import random

from scrapers.base import BaseScraper
from utils.models import Listing


class PsaScraper(BaseScraper):
    source = "psa"

    def fetch(self, card_name: str) -> list[Listing]:
        # PSA contributes grading supply-like records represented as listings.
        return [
            Listing(
                source=self.source,
                card_name=card_name,
                price=0,
                listing_id=f"{card_name}-psa-pop",
                listing_url="https://www.psacard.com/",
                sold_count=random.randint(50, 5000),
            )
        ]
