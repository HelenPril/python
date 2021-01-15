class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        return f'Объединение двух клеток: {Cell(self.cell + other.cell)}'

    def __sub__(self, other):
        res = int(self.cell - other.cell)
        if res >= 0:
            return f'Результат вычитания: {res}'
        else:
            return f'Ошибка! Отрицательное число!'

    def __mul__(self, other):
        return f'Создание одной клетки: {Cell(self.cell * other.cell)}'

    def __truediv__(self, other):
        return f'Деление клетки: {Cell(self.cell // other.cell)}'

    def make_order(self, row):
        kolvo_str = self.cell // row
        kolvo_ostatok =  self.cell % row
        stroka = ''
        for i in range(kolvo_str):
            stroka += f'{"*" * row} \n'
        stroka += f'{"*" * kolvo_ostatok}'
        return f'Ячейки по рядам будут выглядеть: \n' \
               f'{stroka}'

cell_1 = Cell(10)
cell_2 = Cell(15)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(2))
print(cell_1.make_order(4))