#1.
from time import sleep

class TrafficLight:
    #атрибут color (цвет)
    color = ['red', 'yellow', 'green'] # __color = 

    #метод running (запуск)
    def running(self):
        #атрибут реализовать как приватный
        self.__color
    

    def running(self):
        i = 0
        while i < 3:
            print(f'Trafficlight is switching! \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1


# Проверить работу примера, создав экземпляр и вызвав описанный метод.
TrafficLight = TrafficLight()
TrafficLight.running()