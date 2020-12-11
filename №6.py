list = []
analis = {}
name = []
price = []
amount = []
n = int(input('Пожалуйста, укажите сколько товаров вы хотите добавить: '))
x = 1
for i in range(n):
    dict = {'название': input('Пожалуйста, введите название товара: '), 'цена': int(input('Пожалуйста, введите цену товара: ')), 'количество': int(input('Пожалуйста, введите количество товара: ')), 'единицы': 'шт.'}
    corteg = (x, dict)
    x = x + 1
    list.append(corteg)
    name = name + [dict['название']]
    price = price + [dict['цена']]
    amount = amount + [dict['количество']]
    print('*' * 50)
analis = {'название': name, 'цена': price, 'количество': amount, 'единицы': dict.get('единицы')}
print(list)
print(analis)
