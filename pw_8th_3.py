#3.

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input("Enter the value and press 'Enter': "))   #запрашивать у пользователя данные и заполнять список
                self.my_list.append(val)
                print(f'Current list: {self.my_list} \n ')
            except:
                print(f'ValueError - str or boolean')   #вносить его в список, только если введено число
                y_or_n = input(f'Retry one more time? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'U got out'
                else:
                    return f'U got out'

try_except = Error(1)
print(try_except.my_input())