with open('№5_file.txt', 'w+', encoding='utf-8') as infile:
    stroka = ''
    for i in range(1, 101):
        stroka += str(i) + ' '
    print(stroka, file=infile)
    info = stroka.split()
    itog = 0
    for i in range(len(info)):
        itog += int(info[i])
    print('Сумма чисел в данном файле равна: ', itog)