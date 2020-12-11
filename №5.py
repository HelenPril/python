my_list = [7, 5, 3, 3, 2]
n = int(input('Введите число: '))
for i in range(len(my_list)):
    g = int(my_list[i])
    index = len(my_list)
    if n >= g:
        chislo = my_list.count(n)
        if chislo == 0:
            my_list.insert(i, n)
        else:
            my_list.insert(i + chislo, n)
        break
    elif n < int(my_list[index-1]):
        my_list.insert(index, n)
        break
print(my_list)
