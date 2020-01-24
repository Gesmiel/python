#1
name = input('Ваше имя ')
surname = input('Ваша фамилия ')
age = input('Ваш возраст ')
print(f'{name} {surname} {age} лет')

#2
time = int(input('Введите время в секундах '))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time - (hours * 3600  + minutes * 60)
print(f"{hours}:{minutes}:{seconds}сек.")

#3
number = int(input('Введите число '))
print(number + number ** 2 + number **3)

#4
num = input('Введите целое положительное число ')
num_max = num[0]
i = 0
while i < len(num):
    if num[i] > num_max:
        num_max = num[i]
    else:
        i = i + 1
print(num_max)

#5
income = int(input('Выручка '))
cost = int(input('Издержки '))
balance = income - cost
if balance < 0:
    print(f'Убыток {abs(balance)}')
elif balance > 0:
    print(f'Прибыль {abs(balance)}\nРентабельность {round(income/cost,2)}')
    pers = int(input('Количество сотрудников '))
    print(f'Прибыль на одного сотрудника {round(balance/pers,2)}')
else:
    print(f'Работаете в ноль')

#6
a = int(input('Количество километров, которые пробежал спортсмен в 1-ый день '))
b = int(input('Планируемый общий результат спортсмена (в км.) '))
i = 1
while a < b:
    a = a + a/10
    i += 1
print(f'На {i}-й день спортсмен достиг результата не менее {b} км')
