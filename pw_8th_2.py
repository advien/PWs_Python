#2.

#класс-исключение, обрабатывающий ситуацию деления на нуль
class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except ZeroDivisionError:
            return (f"Incorrect division because of null!") #при вводе нуля в качестве делителя

#Проверьте его работу на данных, вводимых пользователем.
a = int(input('Enter the number (divider): '))
b = int(input('Enter the number (denominator): '))
div = DivisionByNull(a, b) 
# print(DivisionByNull.divide_by_null(10, 0)) <-- проверка на ноль без пользователя
# print(DivisionByNull.divide_by_null(10, 0.1)) <-- проверка внутри на разный тип чисел 
print(div.divide_by_null(a, b))
