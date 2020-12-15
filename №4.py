def my_func(x, y):
    if x > 0 and y < 0:
        result_1 = x ** y
        return 'Результат №1 с помощью оператора:', round(result_1, 2)
print(*my_func(2, -3))

def my_func_2(x, y):
    if x > 0 and y < 0:
        y = y * (-1)
        g = x
        for i in range(y-1):
            x = x * g
        result_2 = 1 / x
        return 'Результат №2 с помощью цикла:', round(result_2, 2)
print(*my_func_2(2, -3))