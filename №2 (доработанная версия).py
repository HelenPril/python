from abc import ABC, abstractmethod

class Calculation(ABC):
    def __init__(self, param):
        self.p = param

    @property
    @abstractmethod
    def calc(self):
        pass

    def __add__(self, other):
        return f'Всего необходимо ткани: {round((self.calc + other.calc), 2)}'

class Coat(Calculation):
    def __init__(self, param):
        super().__init__(param)

    @property
    def calc(self):
        needed_c = round((self.p / 6.5 + 0.5), 2)
        print(f'Необходимо ткани на пальто: {needed_c}')
        return needed_c

class Suit(Calculation):
    def __init__(self, param):
        super().__init__(param)

    @property
    def calc(self):
        needed_s = round((self.p * 2 + 0.3), 2)
        print(f'Необходимо ткани на костюм: {needed_s}')
        return needed_s


coat = Coat(7)
suit = Suit(10)
print(coat + suit)

