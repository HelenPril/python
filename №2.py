def check(name, surname, year, town, email, phone):
    info = 'Имя: ' + name + ', ' + 'Фамилия: ' + surname + ', ' + 'Год рождения: ' + year + ', ' + 'Город: ' + town + ', ' + 'Email: ' + email + ', ' + 'Номер телефона: ' + phone + '.'
    return info

print(check(name = 'Иван', surname = 'Иванов', town = 'Москва', year = '2000', email = 'info@gmail.com', phone = '8 (800) 700 77 88'))