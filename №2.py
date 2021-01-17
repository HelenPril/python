class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt

first = input('Введите числитель: ')
second = input('Введите знаменатель: ')

try:
    first = int(first)
    second = int(second)
    if second == 0:
        raise MyOwnEr('Знаменаттель не может быть равен 0!!!')
except (ValueError, MyOwnEr) as err:
    print(err)
else:
    res = first / second
    print('Ваш результат: ', res)


try:
    for i in range(len(list)):
        if list[i].isalpha():
            raise MyOwnEr('В введенных данных присутствуют буквы!')
except MyOwnEr as err:
    print(err)
else:
    print('Данные введены корректно!')