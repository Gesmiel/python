#Не получается красиво писать код, но хоть работает - и то хорошо.

print ('#1')

user_list = []
while True:
    user_text = input("Ввведите текст ")
    user_list.append(user_text+'\n')
    if user_text == "":
        break
with open('task1.txt', 'w') as f:
    f.writelines(user_list)
with open('task1.txt', 'r') as f:
    f.read()


print('#2')

s = 0
with open('task2.txt') as f:
    list = f.readlines()
    for string in list:
        string = string.split()
        w = 0
        for word in string:
            w += 1
        s += 1
        print(f'Количество слов в {s}-ой строке: {w}')
    print(f'Количество строк: {s}')


print('#3')

salary = []
workers = {}
with open('task3.txt') as f:
    list = f.readlines()
    for string in list:
        string = string.split()
        for word in string:
            workers[string[0]] = string[1]

    for key in workers.keys():
        salary.append(int(workers[key]))
        if int(workers[key]) < 25000:
            print(f'У {key}a оклад меньше 25000')

print(string)
average = sum(salary)/len(salary)
print(f'Средний размер оклада составляет {average}')


print('#4')

ru_numb = ['Один', 'Два', 'Три', 'Четыре']
new_line = []
i = 0
with open('task4.txt') as file:
    for line in file:
        item = line.split(' — ')
        item[0] = ru_numb[i]
        new_line.append(item[0] + ' — ')
        new_line.append(item[1])
        i += 1
with open('task4_1.txt', 'w') as new_file:
    new_file.writelines(new_line)


print('#5')

with open('task5.txt', 'w') as f:
    a = input('Введите число ')
    while a.isdigit():
        a = input('Введите число ')
        f.write(a)
        f.write(' ')

with open('task5.txt') as f:
    a = f.read()
    numbers = a.split(' ')
    numbers = [int(el) for el in numbers if el.isdigit()]
print(f'сумма элементов равна {sum(numbers)}')


print('#6')

def my_func(el):
    if '(л)' in el:
        el = el.replace('(л)', '')
        return int(el)
    elif '(пр)' in el:
        el = el.replace('(пр)', '')
        return int(el)
    elif '(лаб)' in el:
        el = el.replace('(лаб)', '')
        return int(el)
    elif el == '—':
        el = 0
        return el

stat = {}
subjects = []
info = []
my_sum = 0
with open('task6.txt') as f:
    a = f.readlines()
    for group in a:
        subject = group.split(':')
        for el in subject[1].split():
            my_sum = my_sum + my_func(el)
            stat[subject[0]] = my_sum
        my_sum = 0

print(stat)


print('#7')

import json

my_dict = []
average = {}
profits = []
stat = {}

with open('task7.txt') as f:
    content = f.read().splitlines()
    for group in content:
        group = group.split()
        profit = int(group[2]) - int(group[3])
        profits.append(profit)
        stat[group[0]] = profit
    new_profits = [item for item in profits if item > 0]
    average['average_profit'] = sum(new_profits)/len(new_profits)
    my_dict.append(stat)
    my_dict.append(average)
    print(my_dict)

with open("companies.json", "w") as write_f:
    json.dump(my_dict, write_f)
