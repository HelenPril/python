from abc import ABC, abstractmethod

class Calculation(ABC):
    def __init__(self, width, height):
        self.w = width
        self.h = height

    @abstractmethod
    def calc(self):
        pass


class Param(Calculation):
    def __init__(self, width, height):
        super().__init__(width, height)

    @property
    def calc(self):
        coat = round((self.w / 6.5 + 0.5), 2)
        suit = round((self.h * 2 + 0.3), 2)
        full = round((coat + suit), 2)
        return(f'Необходимо ткани на пальто: {coat} \n'
               f'Необходимо ткани на костюм: {suit} \n'
               f'Необходимо ткани: {full}')


param = Param(7, 10)
print(param.calc)

