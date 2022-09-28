import concurrent.futures as concurrent_futures
import glob
import multiprocessing
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

BOOK = 'book'
SHEET = 'sheet'
CELL = 'cell'
VALUE = 'value'


def get_books(base: str) -> list:
    if not os.path.isdir(base):
        raise ValueError('ディレクトリではありません')

    # ルールが雑すぎる
    return glob.glob(os.path.join(base, '**', '*.xls*'), recursive=True)


def grep(base: str, condition: str) -> list:
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:

        futures = []
        for book in get_books(base):
            futures.append(executor.submit(find, book, condition))

        merged = []
        for future in concurrent_futures.as_completed(futures):
            for result in future.result():
                merged.append(result)

        return merged


def output(results: list):
    for result in results:
        print('\t'.join([result[BOOK], result[SHEET], result[CELL], result[VALUE]]))


def find(book_name: str, condition: str) -> list[dict]:
    book = openpyxl.load_workbook(book_name, read_only=True, data_only=True)
    try:
        results = []
        for sheet_name in book.sheetnames:
            sheet: Worksheet = book[sheet_name]
            for row in sheet.rows:
                for cell in row:
                    if cell.value is not None and is_matched(cell.value, condition):
                        results.append({
                            BOOK: book_name,
                            SHEET: sheet_name,
                            CELL: cell.coordinate,
                            VALUE: cell.value
                        })
        return results
    finally:
        book.close()


def is_matched(value: str, condition: str) -> bool:
    return condition in value


if __name__ == '__main__':
    args = sys.argv

    try:
        if len(args) != 3:
            raise ValueError('引数が不正')

        matched_list = grep(args[1], args[2])
        output(matched_list)

    except ValueError as e:
        print(e, file=sys.stderr)
        exit(1)
