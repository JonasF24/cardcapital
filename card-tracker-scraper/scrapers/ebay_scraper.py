from __future__ import annotations

import os
import random

from scrapers.base import BaseScraper
from utils.models import Listing


class EbayScraper(BaseScraper):
    source = "ebay"

    def __init__(self) -> None:
        self.app_id = os.getenv("EBAY_APP_ID", "")

    def fetch(self, card_name: str) -> list[Listing]:
        # Replace with official eBay Browse API calls when credentials are configured.
        samples = [
            round(random.uniform(20, 500), 2),
            round(random.uniform(20, 500), 2),
            round(random.uniform(20, 500), 2),
        ]
        return [
            Listing(
                source=self.source,
                card_name=card_name,
                price=price,
                listing_id=f"{card_name}-ebay-{index}",
                listing_url="https://www.ebay.com/",
                sold_count=random.randint(1, 20),
            )
            for index, price in enumerate(samples, start=1)
        ]
