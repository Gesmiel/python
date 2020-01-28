print('#1')
my_list = [23 , '36', 12.3, True]
i = 0
for i in my_list:
    print(f'{i} {type(i)}')

print('#2')
user_list = []
while True:
    element = input("Добавить элемент в список ")
    user_list.append(element)
    if element == '':
        user_list.pop()
        break
print(user_list)
for i in user_list:
    n = user_list
    if len(user_list)%2 == 0:
        user_list[::2], user_list[1::2] = user_list[1::2], user_list[::2]
    else:
        user_list[:-1:2], user_list[1:-1:2] = user_list[1:-1:2], user_list[:-1:2]
print(n)

print('#3 (list)')
user_choice = input('Введите месяц (от 1 до 12) ')
spring = ['3', '4', '5']
winter = ['1', '2', '12']
summer = ['6', '7', '8']
autumn = ['9', '10', '11']
if user_choice in spring:
    print('Весна')
elif user_choice in summer:
    print('Лето')
elif user_choice in autumn:
    print('Осень')
elif user_choice in winter:
    print('Зима')
else:
    print("Нет такого месяца")

print('#3 (dict) Первый вариант')
months = {1:'Зима', 2:'Зима', 12:'Зима',
          3:'Весна', 4:'Весна', 5:'Весна',
          6:'Лето', 7:'Лето', 8:'Лето',
          9:'Осень', 10:'Осень', 11:'Осень'}
user_choice = input('Введите месяц (от 1 до 12) ')
if user_choice.isdigit():
    user_choice = int(user_choice)
    if 1 <= user_choice <= 12:
        a = months[user_choice]
        print(a)
    else:
        print('Нет такого месяца')
else:
    print('Нужно ввести число от 1 до 12')

print('#3 (dict) Второй вариант')
seasons = {'Зима':(12, 1, 2), 'Весна':(3, 4, 5), 'Лето':(6, 7, 8), 'Осень':(9, 10, 11)}
user_choice = input('Введите месяц (от 1 до 12) ')
if user_choice.isdigit():
    user_choice = int(user_choice)
    if 1 <= user_choice <= 12:
        for season in seasons:
            for i in seasons[season]:
                if user_choice == i:
                    print(season)
    else:
        print(f'Не бывает {user_choice}-го месяца')
else:
    print('Нужно ввести число от 1 до 12')

print('#4')
text = (input('Напишите любое предложение ')).split()
i = 1
for word in text:
    if len(word) < 10:
        print(f'{i}. {word}')
        i += 1
    else:
        word = word[:10]
        print(f'{i}. {word}')
        i += 1

print('#5')
my_list = [7, 5, 3, 3, 2]
print(my_list)
element = 0
while element != '':
    element = input("Добавить элемент в список ")
    if element.isdigit():
        element = int(element)
        if element in my_list:
            a = my_list.index(element)
            my_list.insert(a + 1, element)
        else:
            my_list.append(element)
        print(my_list)
    else:
        print(my_list)


print('#6*')
i = 0
my_shop = []
stat_name = []
stat_price = []
stat_quantity = []
stat_unit = []
stat = {'название': stat_name, 'цена': stat_price, 'количество': stat_quantity, 'ед.': stat_unit}
quote = int(input("Сколько товаров вы хотите внести "))
while i < quote:
    name = input('Название товара ')
    price = input('Цена товара ')
    quantity = input('Количество товара ')
    unit = input('Единица измерения товара ')
    stat_name.append(name)
    stat_price.append(price)
    stat_quantity.append(quantity)
    stat_unit.append(unit)
    a = {'название': name, 'цена': price, 'количество': quantity, 'eд.': unit}
    i += 1
    b = (i, a)
    my_shop.append(b)
    print(b)

print('Товары')
for group in my_shop:
    print(group)
print('Статистика')
print(stat)