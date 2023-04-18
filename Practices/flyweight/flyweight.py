from __future__ import annotations
from typing import List, Mapping, Iterable


class IllegalArgumentException(Exception):
    pass


class Cell:
    def __init__(self, row, column, content, context: CellContext):
        self.row = row
        self.column = column
        self.content = content
        self.context = context

    def render(self):
        print(
            f"({self.row, self.column}): {self.content} [{self.context.font_family}/{self.context.font_size}]\n")


class CellContext:
    def __init__(self, font_size, font_family, is_bold):
        self.font_size = font_size
        self.font_family = font_family
        self.is_bold = is_bold

    @property
    def hash_code(self):
        return hash(f'{self.font_size}{self.font_family}{self.is_bold}')


class CellContextFactory:
    cells: Mapping[int, CellContext] = {}

    @staticmethod
    def get_cell_context(font_size, font_family, is_bold) -> CellContext:
        print(
            f'font_size:{font_size}, font_family: {font_family}, is_bold:{is_bold}')
        hash_code = CellContext(font_size, font_family, is_bold).hash_code
        if hash_code in CellContextFactory.cells:
            return CellContextFactory.cells[hash_code]

        print("Creating a new one")
        context = CellContext(font_size, font_family, is_bold)
        CellContextFactory.cells[hash_code] = context
        return CellContextFactory.cells[hash_code]


class SpreadSheet:
    MAX_ROWS = 3
    MAX_COLS = 3

    def __init__(self):
        self.cells: List[List[Cell]] = [[None for y in range(self.MAX_COLS)]
                                        for x in range(self.MAX_ROWS)]

        self.generate_cells()

    def set_content(self, row, col, content: str):
        self.ensure_cell_exists(row, col)

        self.cells[row][col].content = content

    def set_font_familly(self, row, col, font_family):
        self.ensure_cell_exists(row, col)

        cell = self.cells[row][col]
        current_context = cell.context
        context = CellContextFactory.get_cell_context(
            current_context.font_size, font_family, current_context.is_bold)
        self.cells[row][col].context = context

    def ensure_cell_exists(self, row, col):
        if row < 0 or row >= self.MAX_ROWS:
            raise IllegalArgumentException()

        if col < 0 or col >= self.MAX_COLS:
            raise IllegalArgumentException()

    def generate_cells(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                self.cells[row][col] = Cell(
                    row, col, "", self.get_default_context())

    def get_default_context(self):
        return CellContext(12, "Times New Roman", False)

    def render(self):
        for row in range(self.MAX_ROWS):
            for col in range(self.MAX_COLS):
                self.cells[row][col].render()


def main():
    sheet = SpreadSheet()
    sheet.set_content(0, 0, "Hello")
    sheet.set_content(1, 0, "World")
    sheet.set_font_familly(0, 0, "Arial")
    sheet.set_font_familly(2, 0, "Helvetica")
    sheet.render()


if __name__ == '__main__':
    main()
