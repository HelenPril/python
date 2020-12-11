spisok = []
a = 0
while True:
    a = input('Введите значение: ')
    if a == '':
        break
    else:
        spisok.append(a)
g = 0
for i in range(len(spisok)//2):
    spisok[g], spisok[g+1] = spisok[g+1], spisok[g]
    g = g + 2
print(spisok)
