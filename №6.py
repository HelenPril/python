digits = '1234567890'
dict = {}

with open('№6_file.txt', 'r', encoding='utf-8') as infile:
    for line in infile:
        hours = 0
        number = ''
        for i in range(len(line)):
            if line[i] in digits:
                number = number + str(line[i])
                if line[i+1] not in digits:
                    hours += int(number)
                    number = ''
        line = line.split(': ')
        dict[line[0]] = hours

print(dict)