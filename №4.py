from random import randint

direction = ['север', 'юг', 'восток', 'запад']

class Car:
    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.police = is_police

    def go(self):
        print(f'Go - go {self.n}!!!')

    def stop(self):
        print(f'Stop - stop {self.n}!!!')

    def turn(self):
        print(f'Направление: {direction[randint(0,3)]}')

    def show_speed(self):
        print(f'Ваша скорость составляет {self.s}км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Ваша скорость составляет {self.s}км/ч')
        if self.s > 60:
            print('Вам необходимо сбавить скорость! Вы находитесь в городе!')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Ваша скорость составляет: {self.s}км/ч')
        if self.s > 40:
            print('Вам необходимо сбавить скорость! Ограничение для машин обслуживания - 40км/ч!')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

Town_Car = TownCar(70, 'черный', 'Lexus RX', False)
Town_Car.show_speed()
Town_Car.go()
Town_Car.stop()
Town_Car.turn()
print('*' * 100)

Sport_Car = SportCar(170, 'красный', 'Bugatti', False)
Sport_Car.show_speed()
Sport_Car.go()
Sport_Car.stop()
Sport_Car.turn()
print('*' * 100)

Work_Car = WorkCar(30, 'оранжевый', 'KAMAZ', False)
Work_Car.show_speed()
Work_Car.go()
Work_Car.stop()
Work_Car.turn()
print('*' * 100)

Police_Car = PoliceCar(90, 'синий', 'Lada', True)
Police_Car.show_speed()
Police_Car.go()
Police_Car.stop()
Police_Car.turn()
