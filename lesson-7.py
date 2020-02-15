'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные(список списков) для формирования матрицы.
Реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух
объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.'''

'''class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix.__str__(self)


    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.matrix]))

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
m = Matrix(a)
print(m)
print("+")
n = Matrix(b)
print(n)
print('=')
my_sum = m + n
print(my_sum)'''

'''Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.'''

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    def consump(self):
        return f'На всю одежду необходимо {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f} ткани'

    @abstractmethod
    def abstract(self):
        return 'Abstract'


class Coat(Clothes):
    def consump(self):
        return f'Для пошива пальто нужно {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'Abstract'


class Costume(Clothes):
    def consump(self):
        return f'Для пошива костюма нужно {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass

costume = Costume(56)
coat = Coat(100)
print(coat.consump())
print(costume.consump())
print(coat.abstract())


