#1.
class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matr = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matr[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matr]))

#без проверки результата:
my_matr = Matrix([[8, 14, 7],   
                  [3, 11, 23],
                  [46, 50, 12]],
                 [[4, 8, 2],
                  [6, 1, 78],
                  [47, 3, 61]])

print(my_matr.__add__())


#2. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 6.5 + 0.5

    def get_square_j(self):
        return self.height * 2 + 0.3

    @property
    def get_sq_full(self):
        return str(f'General square of textile: \n'
                   f'{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Square for coat: {self.square_c}'


class Jacket(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Square for suit: {self.square_j}'

coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_sq_full) 
print(jacket.get_sq_full)
print(jacket.get_square_c()) #square of coat
print(jacket.get_square_j()) #square of jacket

#3.
class Cell:     #создать класс Клетка
    def __init__(self, quantity): #параметр, соответствующий количеству клеток (целое число) - quantity
        self.quantity = int(quantity)

    def __str__(self):
        return f'Result of operation: {self.quantity * "*"}'


    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Negatively')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))


    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells_1 = Cell(30) #всё это - изменяемые параметры
cells_2 = Cell(18) 
print(cells_1)
print(cells_1 + cells_2)
print(cells_2 - cells_1) #--> можно ли разделять принт'ы Enter'ом для визуального улучшения чтения кода (вопрос)
print(cells_2.make_order(5))
print(cells_1.make_order(10))
print(cells_1 / cells_2)