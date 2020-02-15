#!/usr/bin/python
# -*- coding: utf-8 -*-

print('#1')

from sys import argv

def pay(output, hours, bonus):
    total = output * hours + bonus
    return total
try:
    output = int(argv[1])
    hours = int(argv[2])
    bonus = int(argv[3])

    print('Размер заработной платы {} руб.'.format(pay(output, hours, bonus)))
except IndexError:
    pass


print('#2')

import random
list_1 = []
for i in range(15): list_1.append(random.randint(0, 100))
print(list_1)
i = 0
new_list = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i-1]]
print(new_list)


print('#3')

my_list = [el for el in range(20, 240) if el%20 == 0 or el%21 == 0]
print(my_list)


print('#4')
i = 0
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [my_list[i] for i in range(len(my_list)) if my_list.count(my_list[i]) == 1 ]
print(new_list)


print('#5')
from functools import reduce

def num():
    even = [el for el in range(100, 1001) if el%2 == 0]
    return even

def mult(num1, num2):
    return num1 * num2
print(reduce(mult, num()))


print('#6')
print('#6-A')

from itertools import count, cycle
a = int(input('Начать с '))

for i in count(start=a, step=1):
    if i > a + 10:
        break
    print(i)

print('#6-B')

i = 0
for el in cycle(['Привет!', 'Как дела ?']):
    if i > 5:
        break
    print(el)
    i += 1


print('#7')

def fact(n):
    i = 1
    for el in range(1, n + 1):
        i = i*el
        yield i

n = int(input('Факториал какого числа? '))

for i in fact(n):
   print(i)




