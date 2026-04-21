from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, Field


class Listing(BaseModel):
    source: str
    card_name: str
    price: float
    currency: str = "USD"
    sold_count: int = 0
    listing_id: str
    listing_url: str = ""
    captured_at: datetime = Field(default_factory=datetime.utcnow)


class EnrichedSnapshot(BaseModel):
    source: str
    card_name: str
    avg_price: float
    min_price: float
    max_price: float
    volume: int
    sentiment: str
    investment_score: float
    generated_at: datetime = Field(default_factory=datetime.utcnow)
