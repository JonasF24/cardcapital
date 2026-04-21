from __future__ import annotations

import os
import random

from scrapers.base import BaseScraper
from utils.models import Listing


class CardMarketScraper(BaseScraper):
    source = "cardmarket"

    def __init__(self) -> None:
        self.token = os.getenv("CARDMARKET_APP_TOKEN", "")

    def fetch(self, card_name: str) -> list[Listing]:
        return [
            Listing(
                source=self.source,
                card_name=card_name,
                price=round(random.uniform(15, 350), 2),
                currency="EUR",
                listing_id=f"{card_name}-cm-{idx}",
                listing_url="https://www.cardmarket.com/",
                sold_count=random.randint(1, 40),
            )
            for idx in range(1, 4)
        ]
