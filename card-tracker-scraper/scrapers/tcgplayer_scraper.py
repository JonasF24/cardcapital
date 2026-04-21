from __future__ import annotations

import os
import random

from scrapers.base import BaseScraper
from utils.models import Listing


class TcgPlayerScraper(BaseScraper):
    source = "tcgplayer"

    def __init__(self) -> None:
        self.public_key = os.getenv("TCGPLAYER_PUBLIC_KEY", "")
        self.private_key = os.getenv("TCGPLAYER_PRIVATE_KEY", "")

    def fetch(self, card_name: str) -> list[Listing]:
        base = random.uniform(10, 200)
        return [
            Listing(
                source=self.source,
                card_name=card_name,
                price=round(base * factor, 2),
                listing_id=f"{card_name}-tcg-{idx}",
                listing_url="https://www.tcgplayer.com/",
                sold_count=random.randint(1, 50),
            )
            for idx, factor in enumerate((0.9, 1.0, 1.1), start=1)
        ]
