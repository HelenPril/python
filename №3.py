class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.n = name
        self.s = surname
        self.p = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'Имя работника: {self.n} {self.s}')

    def get_total_income(self):
        print('Итоговая зарплата:', self._income.get('wage') + self._income.get('bonus'))

result = Position('Иван', 'Иванов', 'директор', 100000, 20000)
result.get_full_name()
result.get_total_income()
