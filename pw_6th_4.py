#4.
class Car:
    # У данного класса должны быть следующие атрибуты:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # А также методы:
    def go(self):
        return f'{self.name} is started'    # машина поехала

    def stop(self):
        return f'{self.name} is stopped'    # остановилась

    # повернула (куда): turn(direction) - turn_right and turh_left
    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    # Добавьте в базовый класс метод show_speed
    def show_speed(self):
        return f'Current speed of {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        # сообщение о превышении скорости:
        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        # сообщение о превышении скорости:
        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


audi = SportCar(140, 'Red', 'Audi', False)
kia = TownCar(30, 'White', 'Kia', False)
lada = WorkCar(70, 'Green', 'Lada', True)
ford = PoliceCar(120, 'Blue', 'Ford', True)
print(audi.turn_right())
print(f'{kia.stop()} when {audi.turn_right()}')
print(f'{lada.go()}')
print(f'{lada.show_speed()}')
print(f'{kia.name} is {kia.color}')
print(f'Is {audi.name} a police car? {audi.is_police}')
print(f'Is {lada.name}  a police car? {lada.is_police}')
print(audi.show_speed())
print(kia.show_speed())
print(ford.police())
print(ford.show_speed())