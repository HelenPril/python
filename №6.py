from itertools import count, cycle

from sys import argv

script_name, floor, ceiling, repeat_amount = argv

print(f'Итак, согласно введенной информации: \nНижнее значение: {(int(floor))}; \nверхнее значение: {(int(ceiling))}; \nожидаемое количество повторений: {(int(repeat_amount))}')

list = []
for i in count(int(floor)):
    if i > int(ceiling):
        break
    else:
        list += [i]
print('Значения в заданном диапазоне:', list)


repeat_amount = int(repeat_amount)
print(f'Делаем повторения из полученного нами списка заданное количество раз ({repeat_amount}):')
for i in cycle(list):
    if repeat_amount == 0:
        break
    print(i)
    repeat_amount -= 1

