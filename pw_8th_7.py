#7.

class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Sum of z1 and z2: ')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Product of z1 and z2: ')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


#Проверьте корректность полученного результата.
z_1 = ComplexNumber(4, -7)
z_2 = ComplexNumber(1, 6)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)