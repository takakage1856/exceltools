from __future__ import annotations

from abc import ABC, abstractmethod


class BaseBook(ABC):
    book_path: str

    def __init__(self, book_path: str):
        self.book_path = book_path

    @abstractmethod
    def find(self, keyword: str) -> list[dict]:
        pass
