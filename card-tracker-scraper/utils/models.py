from __future__ import annotations

from datetime import datetime, timezone
from pydantic import BaseModel, Field


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


class Listing(BaseModel):
    source: str
    card_name: str
    price: float
    currency: str = "USD"
    sold_count: int = 0
    listing_id: str
    listing_url: str = ""
    captured_at: datetime = Field(default_factory=_utcnow)


class EnrichedSnapshot(BaseModel):
    source: str
    card_name: str
    avg_price: float
    min_price: float
    max_price: float
    currency: str = "USD"
    fx_base_currency: str | None = None
    fx_rate: float | None = None
    volume: int
    sentiment: str
    investment_score: float
    generated_at: datetime = Field(default_factory=_utcnow)
