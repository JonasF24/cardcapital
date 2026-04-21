from __future__ import annotations

from abc import ABC, abstractmethod

from utils.models import Listing


class BaseScraper(ABC):
    source: str

    @abstractmethod
    def fetch(self, card_name: str) -> list[Listing]:
        raise NotImplementedError
