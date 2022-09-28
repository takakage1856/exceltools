import openpyxl
from openpyxl import Workbook
from src.model.base_book import BaseBook


class OpenBook(BaseBook):
    book: Workbook

    def __init__(self, book_path: str):
        super().__init__(book_path)
        self.book = openpyxl.load_workbook(book_path, read_only=True, data_only=True)

    def find(self, keyword: str) -> list[dict]:
        pass
