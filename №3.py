with open('№3_file.txt', 'r', encoding='utf-8') as infile:
    vsego = 0
    workers = 0
    for line in infile:
        info = line.split()
        vsego += int(info[1])
        workers += 1
        if int(info[1]) >= 20000:
            print(f'У {info[0]}а зарпалата больше 20000 рублей, а именно {info[1]} рублей')
print(f'Средняя зарплата: {round(vsego / workers)}')