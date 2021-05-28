# 1.
user_age = 'Stranger'
user_weight = 0.0
print(user_age, user_weight, sep=',')

user_name = input('Enter your name: ')
user_lastname = input('Enter your lastname: ')
user_age = int(input('Enter your age: '))
user_weight = float(input('Enter your weight: '))

print('Hi,', user_name, user_lastname, ',', user_age, 'y.o.', 'I know, your weight is', user_weight, 'I know everything, haha!')


# 2.
time = int(input('Enter the time (sec): '))
print('{0:02d} {1:02d} {2:02d}'.format(time // 3600, time % 3600 // 60, time % 60))


# 3.
n = int(input('Enter the number: '))
print(n + n*11 + n*111)


# 4.
n = int(input('Enter an integer positive number: '))
max = 0

while True:
    a_n = n % 10
    if a_n > max:
        max = a_n
    n //= 10
    if n == 0:
        break
print('Max number of the digit: ', max)


# 5.
proceeds = float(input('Enter the proceeds: '))
costs = float(input('Enter the costs: '))
income = proceeds - costs
outcome = -income
if proceeds > costs:
    profitability = (income / proceeds) * 100
    population = int(input("Company's population: "))
    pro_for_one = income / population
    print('Finance result: income, ', income, '\n', 'Profitability: ', profitability, '% \n', 'An income of company for one employee', pro_for_one)
else: 
    print('Finance result: outcome, ', outcome)


# 6.
a = int(input('Enter your result: '))
b = int(input('Enter your aim: '))
n = 1
print( '{}-й день: {}'.format(n, a))

while a < b:
    a *= 1.1
    n += 1
    print( '{}-й день: {}'.format(n, a))
print('Ответ: на ', n, '-й день спортсмен достиг результата — не менее ', b,' км.')

input()
