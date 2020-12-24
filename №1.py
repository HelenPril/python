with open('new_file.txt', 'w', encoding='utf-8') as infile:
    while True:
        line = input('Введите данные: ')
        if line == '':
            break
        else:
           print(line, file=infile)