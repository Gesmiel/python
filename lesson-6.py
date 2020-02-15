"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт."""

from time import sleep
from itertools import cycle


class TrafficLight:
    __color = []

    def add_color(self, color):
        self.__color.append(color)

    def running(self):
        i = 0
        for el in cycle(TrafficLight.__color):
            i += 1
            if i > 6:
                break
            if el == 'Красный' and el == TrafficLight.__color[0]:
                print(el)
                sleep(7)
            elif el == 'Жёлтый' and el == TrafficLight.__color[1]:
                print(el)
                sleep(2)
            elif el == 'Зелёный' and el == TrafficLight.__color[2]:
                print(el)
                sleep(5)
            else:
                break


f = TrafficLight()
f.add_color('Красный')
f.add_color('Жёлтый')
f.add_color('Зелёный')
f.running()

"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
Проверить работу метода.
Например: 20м*5000м*25кг*5см = 12500 т"""

class Road:
    def __init__(self, legth, wigth):
        self._length = legth
        self._width = wigth
        self.weight = 25
        self.height = 5

    def calc_mass(self):
        mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия дорожного полотна необходимо  {int(mass)} т. асфальта')

a = Road(5000, 20)
a.calc_mass()


"""Реализовать базовый класс Worker, в котором определить атрибуты: name, surname, position,
income. Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position на базе класса Worker. В классе Position
реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров)."""


income = {'wage': 100000, 'bonus': 500}

class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.position} {self.name} {self.surname}')

    def get_total_income(self):
        total_income = int(income['wage']) + int(income['bonus'])
        print(f'Заработная плата с учетом премии равна {total_income} рублей')


a = Position('Александр', 'Фомин', 'Гроза офиса')
a.get_full_name()
a.get_total_income()


"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, 
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат."""


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name}. Цвет: {self.color}. Едет')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость автомобиля {self.name} выше разрешенной на {int(self.speed) - 60} км/ч')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость автомобиля {self.name} выше разрешенной на {int(self.speed) - 40} км/ч !')


class PoliceCar(Car):
    pass


a = TownCar('Dodge', 'чёрный', 75, False)
a.go()
a.show_speed()
a.turn('налево')
a.stop()

print('-------------------------------------------')

a = WorkCar('Камаз', 'красный', 50, False)
a.go()
a.show_speed()
a.turn('направо')
a.stop()

print('-------------------------------------------')

a = SportCar('Nissan GT-R', 'белый', 240, False)
a.go()
a.show_speed()
a.turn('налево')
a.stop()

print('-------------------------------------------')

a = PoliceCar('Ваз', 'серебристый', 59, True)
a.go()
a.show_speed()
a.turn('направо')
a.turn('налево')
a.stop()


"""Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen('ручкой')
pen.draw()
pencil = Pencil('карандашём')
pencil.draw()
handle = Handle('маркером')
handle.draw()