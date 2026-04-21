from __future__ import annotations

import hashlib
import time
from collections.abc import Iterable

from utils.models import Listing


class RateLimiter:
    def __init__(self, delay_seconds: float = 0.5) -> None:
        self.delay_seconds = delay_seconds

    def wait(self) -> None:
        time.sleep(self.delay_seconds)


def listing_fingerprint(listing: Listing) -> str:
    payload = f"{listing.source}|{listing.listing_id}|{listing.card_name}|{listing.price}"
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def deduplicate(listings: Iterable[Listing]) -> list[Listing]:
    seen: set[str] = set()
    unique: list[Listing] = []
    for listing in listings:
        fingerprint = listing_fingerprint(listing)
        if fingerprint in seen:
            continue
        seen.add(fingerprint)
        unique.append(listing)
    return unique
