class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt

print('Введите данные. Для остановки нажмите "q"!')
list = []
while True:
    n = input()
    if n == 'q':
        break
    else:
        try:
            if n.isalpha():
                raise MyOwnEr('Должны вводиться лишь цифры!')
        except MyOwnEr as err:
            print(err)
        else:
            list += [n]

print('Получившийся список: ', *list)