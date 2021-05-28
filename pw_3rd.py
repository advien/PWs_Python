#1.
def div(*args):

    try:
        arg_1 = int(input("Input dividend: "))
        arg_2 = int(input("Input divider: "))
        res = arg_1 / arg_2
    except ValueError:
        return 'Value error.'
    except ZeroDivisionError:
        return "Wrong devider! You can't use zero as a devider."

    return res

    #для нуля:
    if arg2 != 0:
        return arg1 / arg2
    else:
        print("Wrong number! Devider can't be null/")


print(f'result  {div()}')

#2.
name = input('Enter name: ')
surname = input('Enter surname: ')
year = int(input('Enter year: '))
city = input('Enter city: ')
email = input('Enter email: ')
telephone = input('Input telephone: ')

def my_func (name, surname, year, city, email, telephone):
     return ' '.join([name, surname, year, city, email, telephone])
print(my_func(surname = 'Vien', name = 'D', year = '2002', city = 'St.Petersburg', email = 'non_name@mail.ru', telephone = '8-9xx-xxx-xx-xx'))

#3.
def my_func(arg_1 , arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3

print(f'Result - {my_func(int(input("Enter the first argument: ")), int(input("Enter the second argument: ")), int(input("Enter the third argument: ")))}')

#4.
def my_func_1(x, y):
    return x ** y;
def my_func_2(x, y):
    result = 1
    while y < 0:
        result /= x
        y += 1
    return result;

#Проверим функции
print(my_func_1(2, -4))
print(my_func_2(2, -4))

#5.
def my_sum ():
    sum_result = 0
    ex = False
    while ex == False:
        number = input('Input numbers or Q for quit: ').split()

        result = 0
        for elem in range(len(number)):
            if number[elem] == 'q' or number[elem] == 'Q':
                ex = True
                break
            else:
                result = result + int(number[elem])
        sum_result = sum_result + result
        print(f'Current sum is {sum_result}.')
    print(f'Your final sum is {sum_result}.')
my_sum()

#6.
def int_func(words):  #задаём аргументы
    result = ""
    for word in words:
        word = word[0].upper() + word[1:]
        result += word + " "
    return result

string = input('Enter the string consists of words splited with space where each word is latin word in lower reg: ')
print(int_func(string.split()))