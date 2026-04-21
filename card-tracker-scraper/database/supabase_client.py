from __future__ import annotations

import os

from supabase import Client, create_client

from utils.models import EnrichedSnapshot, Listing


class SupabaseStore:
    def __init__(self) -> None:
        self.url = os.getenv("SUPABASE_URL", "")
        self.key = os.getenv("SUPABASE_KEY", "")
        self.client: Client | None = None
        if self.url and self.key:
            self.client = create_client(self.url, self.key)

    def upsert_listings(self, listings: list[Listing]) -> None:
        if not self.client:
            return
        payload = [item.model_dump(mode="json") for item in listings]
        self.client.table("market_listings").upsert(payload).execute()

    def upsert_snapshots(self, snapshots: list[EnrichedSnapshot]) -> None:
        if not self.client:
            return
        payload = [item.model_dump(mode="json") for item in snapshots]
        self.client.table("market_snapshots").upsert(payload).execute()
