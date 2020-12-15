def my_func(arg_1, arg_2, arg_3):
    sum_1 = arg_1 + arg_2
    sum_2 = arg_1 + arg_3
    sum_3 = arg_2 + arg_3
    maxim = max(sum_1, sum_2, sum_3)
    return 'Сумма самых больших чисел: ', maxim

print(*my_func(10, 20, 30))
