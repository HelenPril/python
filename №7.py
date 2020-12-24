import json

dict = {}
vsego_dohod = 0
kolvo_firm = 0
spisok = []

with open('№7_file.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        line = line.replace('.', '')
        line = line.split()
        profit = int(line[2]) - int(line[3])
        dict[line[0]] = profit
        vsego_dohod += int(profit)
        kolvo_firm += 1

average = vsego_dohod // kolvo_firm
dict['average_profit'] = average
spisok.append(dict)

with open('json_file.json', 'w', encoding='utf-8') as infile:
    json.dump(spisok, infile)
