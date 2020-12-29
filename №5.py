class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы используете инструмент: {self.t}. Будем рисовать ручкой!')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы используете инструмент: {self.t}. Будем рисовать карандашом!')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Вы используете инструмент: {self.t}. Будем рисовать маркером!')

pen = Pen('ручка')
pen.draw()
print('*' * 100)

pencil = Pencil('карандаш')
pencil.draw()
print('*' * 100)

handle = Handle('маркер')
handle.draw()
