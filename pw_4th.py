#1.
def my_salary():
    try:
        time = float(input('Output in hours: '))
        salary = int(input('Hourly rate: '))
        bonus = int(input('Bonus: '))
        res = time * salary + bonus
        print(f'заработная плата сотрудника  {res}')
    except ValueError:
        return print('Not a numberю')
my_salary()

#2.
my_list = [19, 5, 7, 4, 7, 5, 4, 19]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Original list: {my_list}')
print(f'New list: {my_new_list}')

#3.
print(f'Числа от 20 до 240 кратные 20 или 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

#4. 
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)

#5.
from functools import reduce

def my_func(el_prev, el):
    return el_prev * el

print(f'The list of even values: {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'The result of multiplying all the elements of the list: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')

#6.
from itertools import count

с = 0
for el in count(int(input('Enter the start number: '))):
    if с > 10:
        break
    print(el)
    с += 1

from itertools import cycle

my_list = [True, 'ABC', 123, None]
с = 0

for el in cycle(my_list):
    if с > 10:
        break
    print(el)
    с += 1

#7.
from itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
g = 0
for i in gen:
    if g < 15:
        print(i)
        g += 1
    else:
        break 