# 1.
my_list = ['hello', 2, True]

for element in my_list:
    print(type(element))


# 2.
my_list = list(input('Enter the numbers or words splited with space: ').split())
j = 0

for i in range(int(len(my_list)/2)):
  my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
  j += 2
 
print(my_list)


# 3.
# вывод через list и dict:
seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
month = int(input("Enter a month with number: "))
if month == 12 or month == 1 or month == 2:
  print(seasons_list[0])
  print(seasons_dict.get(1))
elif month == 3 or month == 4 or month ==5:
  print(seasons_list[1])
  print(seasons_dict.get(2))
elif month == 6 or month == 7 or month == 8:
  print(seasons_list[2])
  print(seasons_dict.get(3))
elif month == 9 or month == 10 or month == 11:
  print(seasons_list[3])
  print(seasons_dict.get(4))
else:
  print("This month doesn't exist.") 


# 4.
my_str = (input('Enter the words: '))
ent_word = []
num = 1
for elem in range(my_str.count(' ') + 1):
    ent_word = my_str.split()
    if len(str(ent_word)) <= 10:
        print("{0} {1}".format(num, ent_word[elem])) #у меня компилятор ниже 3.6 версии, поэтому так записываю "format"
        num += 1
    else:
        print("{0} {1}".format(num, ent_word[elem] [0:10])) #если нужно и для >= 3.6 ver.: print(f" {num} {ent_word[elem] [0:10]}") 
        num += 1


# 5.
my_list = [7, 5, 3, 3, 2]
print(f"Rating: {my_list}") #обновил версию...
digit = int(input("Enter the number (don't cross the max number - 100): "))
while digit != 100:
    for elem in range(len(my_list)):
        if my_list[elem] == digit:
            my_list.insert(elem + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[elem] > digit and my_list[elem + 1] < digit:
            my_list.insert(elem + 1, digit)
    print(f"Rating for now: {my_list}")
    digit = int(input("Enter the number (cross the max number 100 for break): "))


# 6.
goods = []
features = {'name': '', 'price': '', 'quantity': '', 'unit': ''}
analytics = {'name': [], 'price': [], 'quantity': [], 'unit': []}
feature_one = None
manage = None
num = 0
while True:
    manage = input("For quit press 'Q', for continue press 'Enter', for analytics press 'A'\n").upper()
    if manage == 'Q':
        break
    num += 1
    if manage == 'A':
        print(f'\n Current analytics: \n {"-" * 30}')
        for key, value in analytics.items():
            print(f'{key[:20]:>30}: {value}')
            print("-" * 30)
    for f in features.keys():
        feature_one = input(f'Input feature: "{f}"')
        features[f] = int(feature_one) if (f == 'price' or f == 'quantity') else feature_one
        analytics[f].append(features[f])
    goods.append(num) #не разрешил два сразу. пришлось разделить. почему так?
    goods.append(features)