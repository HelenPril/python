dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
itog = []

with open('№4_file.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        line = line.strip()
        info = line.split(' ')
        itog.append(dict[info[0]] + ' ' + info[1] + ' ' + info[2])
    print(itog)

with open('translate.txt', 'w', encoding='utf-8') as infile:
    for i in range(len(itog)):
        print(itog[i], file=infile)