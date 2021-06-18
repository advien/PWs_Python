#4.

# Не совсем уловил суть этого предложения: "Создайте класс, описывающий склад.
# По сути, класс "Оргтехника" и его классы-наследники и формируют "склад"?

class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'The device model': self.name, 'The price for one item': self.price, 'Quantity': self.quantity}

    def __str__(self):
        return f'{self.name} price - {self.price} quantity - {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        print(f"Press: 'Q' to way out, 'Enter' to continue")
        while True:
            try:
                unit = input(f'Enter the product name: ')
                unit_p = int(input(f'Enter the price for one item: '))
                unit_q = int(input(f'Enter quantity: '))
                unique = {'The device model: ': unit, 'The price for one item: ': unit_p, 'Quantity: ': unit_q}
                self.my_unit.update(unique)
                self.my_store.append(self.my_unit)
                print(f'Currwnt list: -\n {self.my_store}')
            except:
                return f'Error of data input'

        print(f"Press: 'Q' to way out, 'Enter' to continue")
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'All of storage: -\n {self.my_store_full}')
            return f'Way out'
        else:
            return OfficeEquipment.reception(self)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'To print smth {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'To scan smth {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'To copier smth {self.numb} times'


unit_1 = Printer('hp', 5000, 1, 10)
unit_2 = Scanner('Canon', 2000, 2, 10)
unit_3 = Copier('Xerox', 3000, 1, 10)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
