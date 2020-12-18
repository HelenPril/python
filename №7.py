from math import factorial

def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)
    yield 'Факториал введенного числа:', factorial(n)

n = int(input('Введите число, факториал которого хотите найти:'))

itog = [el for el in fact(n)]
print(*itog)