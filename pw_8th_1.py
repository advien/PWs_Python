#1.

#Реализовать класс «Дата»
class Date:
    #функция-конструктор
    def __init__(self, day_month_year):
        #self.day = day
        #self.month = month
        #self.year = year
        
        #принимать дату в виде строки формата 
        self.day_month_year = str(day_month_year)

    #В рамках класса реализовать два метода.
    @classmethod    #должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i) #«день-месяц-год»

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod   #должен проводить валидацию числа, месяца и года.
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2021:   #2021 >= year >= 0
                    return f'All right!'
                else:
                    return f'Incorrect year!'
            else:
                return f'Incorrect month!'
        else:
            return f'Incorrect day!'

    def __str__(self):
        return f'The current day: {Date.extract(self.day_month_year)}'


#Проверить работу полученной структуры на реальных данных.
today = Date('26 - 4 - 2002')
print(today)
print(Date.extract('11 - 22 - 2022')) #извлекаeт
print(today.extract('21 - 11 - 2021')) #извлекаeт
print(Date.valid(11, 22, 2022)) #валидация
print(today.valid(3, 13, 2003)) #валидация
print(Date.valid(1, 1, 2001)) #валидация