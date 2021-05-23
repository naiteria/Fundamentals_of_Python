class Cell:
    cells_number: int

    def __init__(self, cells_number: int):
        self.cells_number = int(cells_number)

    def __add__(self, other):
        return Cell(self.cells_number + other.cells_number)

    def __sub__(self, other):
        return Cell(self.cells_number - other.cells_number)

    def __mul__(self, other):
        return Cell(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        if other.cells_number == 0:
            return f'Нельзя делить на ноль!\n'
        else:
            return Cell(self.cells_number / other.cells_number)

    def __str__(self):
        return f'Количество клеток после проведенной операции: {self.cells_number * "*"} ({self.cells_number})'

    def make_rows(self, cells_in_row):
        row = 'Организация ячеек по рядам:\n'

        for i in range(round(int(self.cells_number) / cells_in_row)):
            row += f'{cells_in_row * "*"}\n'
        row += f'{(int(self.cells_number) % cells_in_row) * "*"}\n'
        return row


a = Cell(13)
b = Cell(6)
c = Cell(0)

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a / c)

print(a.make_rows(5))
print(b.make_rows(5))
