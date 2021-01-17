class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        # сделано для красоты и читабельности результатов
        if self.b + other.b < 0:
            return f'Сумма равна: {self.a + other.a}{self.b + other.b}i'
        else:
            return f'Сумма равна: {self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        # сделано для красоты и читабельности результатов
        if self.b * other.a < 0:
            return f'Произведение равно: {self.a * other.a - (self.b * other.b)}{self.b * other.a}i'
        else:
            return f'Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'


z_1 = ComplexNumber(4, 5)
z_2 = ComplexNumber(12, -7)
print(z_1 + z_2)
print(z_1 * z_2)