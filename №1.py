class Data:
    def __init__(self, date):
        self.d = date

    @classmethod
    def transform(cls, date):
        date = date.split('-')
        day = int(date[0])
        month = int(date[1])
        year = int(date[2])
        return f'{day}.{month}.{year}'

    @staticmethod
    def valid(day, month, year):
        if day >= 1 and day <= 31 and month >= 1 and month <= 12 and year >= 0 and year <= 2021:
            return 'Все данные введены корректно!'
        else:
            return 'Ошибка! Проверьте правильность введенных данных!'

    def __str__(self):
        return f'Введенная дата: {Data.transform(self.d)}'

your_data = Data('17-1-2021')
print(your_data)
print(Data.valid(78, 1, 2020))
print(Data.valid(2, 12, 2021))