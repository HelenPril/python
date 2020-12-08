n = int(input('Введите число: '))
g = 0
while n != 0:
    last_num = n % 10
    n = n // 10
    if last_num >= g:
        g = last_num
    else:
        g = g
print('Наибольшее число: ', g)