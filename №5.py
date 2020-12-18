from functools import reduce

def function(arg_1, arg_2):
    return arg_1 * arg_2

list = [el for el in range(100, 1001) if el % 2 == 0]

print('Результат умножения:', reduce(function, list))
