def division(arg_1, arg_2):
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
    except ValueError:
        print('*' * 50)
        return 'ValueError'
    try:
        result = arg_1 / arg_2
        print('*' * 50)
        return 'Результат: ', round(result, 2)
    except ZeroDivisionError:
        print('*' * 50)
        return 'Делить на 0 нельзя!'

print(division(input('Введите первое число: '), input('Введите второе число: ')))