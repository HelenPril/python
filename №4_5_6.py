class Warehouse:
    def __init__(self, lenght, width, price_m):
        self.l = lenght
        self.w = width
        self.pM = price_m

    def razmer(self):
        return f'Площадь нашего склада составляет: {self.l * self.w} кубических метров'

    def rent(self):
        return f'Стоимость аренды составляет: {self.l * self.w * self.pM} рублей'


class OfficeEquipment:
    def __init__(self, name, price, quantity, *args):
        self.n = name
        self.p = price
        self.q = quantity
        self.info = {'Наименование товара': self.n, 'Цена товара': self.p, 'Количество': self.q}

    def reception(self):
        full = []
        while True:
            print('Введите данные о товаре (наименование, цена, количество)')
            try:
                enter_n = input('Наименование товара: ')
                enter_p = int(input('Цена товара: '))
                enter_q = int(input('Количество товара: '))
            except ValueError:
                print('Введены неверные данные! Цена и количество товара может содержать лишь числа. Повторите попытку!')
            else:
                info = {'Наименование товара': enter_n, 'Цена товара': enter_p, 'Количество': enter_q}
                full += [info]
            a = input('Для выхода нажмите "q", Для продолжения "Enter"')
            if a == 'q' or a == 'Q':
                break

        full += [self.info]

        return f'Сейчас на складе: {full}'

class Printer(OfficeEquipment):
    def purpose(self):
        return f'Принтер {self.n} необходим для печати документов'

class Scanner(OfficeEquipment):
    def purpose(self):
        return f'Сканер {self.n} необходим для сканирования документов'

class Copier(OfficeEquipment):
    def purpose(self):
        return f'Ксерокс {self.n} необходим для копирования документов'


warehouse = Warehouse(20, 30, 500)
print(warehouse.razmer())
print(warehouse.rent())

printer = Printer('hp', 2000, 5)
scanner = Scanner('Nikon', 1200, 5)
copier = Copier('Xerox', 1500, 1)
print(printer.reception())
print(printer.purpose())
print(scanner.purpose())
print(copier.purpose())