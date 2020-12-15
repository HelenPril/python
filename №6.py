""""Первая часть задачи"""

def int_func(slovo):
    k = slovo[0]
    k = k.upper()
    slovo_new = k
    for i in range(1, len(slovo)):
        slovo_new = slovo_new + slovo[i]
    return 'Новое слово:', slovo_new
print(*int_func('text'))


""""Вторая часть задачи"""

def int_func_2(stroka):
    stroka = stroka.split()
    stroka_new = ''
    for i in range(len(stroka)):
        k = stroka[i][0]
        k = k.upper()
        slovo_new = k
        for g in range(1, len(stroka[i])):
            slovo_new = slovo_new + stroka[i][g]
        stroka_new = stroka_new + slovo_new + ' '
    return 'Новая строка:', stroka_new
print(*int_func_2('cat dog house'))


""""Вторая часть задачи легким способом"""
print('*' * 50)

def int_func_2(*args):
    words = input('Введите слова через пробел: ')
    stroka = words.title()
    return 'Новая строка 2.0:', stroka
print(*int_func_2())