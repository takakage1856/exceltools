from src.model.base_book import BaseBook
from xlwings import Book


class LegacyBook(BaseBook):
    book: Book

    def __init__(self, book_name: str, book_path: str):
        super().__init__(book_path)
        self.book = Book(book_name)

    def find(self, keyword: str) -> list[dict]:
        for sheet in self.book.sheets:
            print(sheet)

        return []
