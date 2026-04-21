from __future__ import annotations

from statistics import mean

from utils.models import EnrichedSnapshot, Listing


class GeminiEnricher:
    def enrich(self, source: str, card_name: str, listings: list[Listing]) -> EnrichedSnapshot:
        prices = [entry.price for entry in listings if entry.price > 0]
        if not prices:
            prices = [0.0]
        avg_price = mean(prices)
        score = min(100.0, max(0.0, avg_price / 5))
        sentiment = "bullish" if score >= 50 else "neutral"
        return EnrichedSnapshot(
            source=source,
            card_name=card_name,
            avg_price=round(avg_price, 2),
            min_price=round(min(prices), 2),
            max_price=round(max(prices), 2),
            volume=sum(item.sold_count for item in listings),
            sentiment=sentiment,
            investment_score=round(score, 2),
        )
