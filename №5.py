def summa():
    vsego = 0
    proverka = False
    while proverka == False:
        stroka = input().split()
        summa_str = 0
        for i in range(len(stroka)):
            if stroka[i] == 'Q' or stroka[i] == 'q':
                proverka = True
                print('Вы вышли из программы. Финальный результат:')
                break
            else:
                summa_str = summa_str + int(stroka[i])
        vsego = vsego + summa_str
        print(f'{summa_str} ({vsego})')

summa()