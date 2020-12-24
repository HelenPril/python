with open('№2_file.txt', 'r', encoding='utf-8') as infile:
    kolvo_str = 0
    i = 1
    for line in infile:
        new_line = line.split()
        kolvo_slov = len(new_line)
        print(f'В {i} строке {kolvo_slov} слов')
        kolvo_str += 1
        i += 1
print('Всего строк в данном тексте:', kolvo_str)