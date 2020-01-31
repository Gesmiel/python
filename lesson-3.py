print('#1')

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("На ноль делить нельзя!")


a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
print(division(a, b))


print('#2')

def person(name, surname, birth_year, city, email, phone):
    print(f'{name} {surname} {birth_year}г.р, г.{city} {email} тел.{phone}')


person(name = input('Введите имя '),
surname = input('Введите фамилию '),
birth_year = input('Введите год рождения '),
city = input('Введите город проживания '),
email = input('Введите email '),
phone = input('Введите номер телефона '))


print('#3')

def big_sum(a, b, c):
    s = [a, b, c]
    big = sorted(s)[-2:]
    return big[0] + big[1]

print(big_sum(3, 4, 5))


print('#4')

#Первый вариант
def my_func_1(x, y):
    return x**y

#Второй вариант
def my_func_2(x, y):
    i = 1
    while y < 0:
        i = i * 1 / x
        y = y + 1
    return i

x = abs(int(input('Введите х ')))
y = abs(int(input('Введите y ')))*-1
print(my_func_1(x, y))
print(my_func_2(x, y))


print('#5')

def user_sum(numbers):
    global my_sum
    global stop
    for number in numbers:
        if number.isdigit():
            number = int(number)
            my_sum = my_sum + number
        elif number == 'stop'.lower():
            stop = 1
            break
    return my_sum


stop = 0
my_sum = 0
numbers = None
while numbers != 'stop'.lower():
    numbers = (input('Введите числа ')).split()
    print(user_sum(numbers))
    if stop == 1:
        break


print('#6')

def int_func(word):
    return word[0].upper() + word[1:]

word = input('Введите слово ')
print(int_func(word))

words = (input('Введите строку ')).split()
up_words = []

for word in words:
    word = int_func(word)
    up_words.append(word)

print(' '.join(up_words))






