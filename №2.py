class Road:
    def __init__(self, length, width):
        self._l = length
        self._w = width

    def formula(self):
        return (f'Вам необходимо {(self._l * self._w * 25 * 5) // 1000}т')

result = Road(5000, 20)
print(result.formula())
