import time


class TrafficLight:
    def __init__(self):
        self.__color = ""
        self.__all_colors = (("\033[31mКрасный", 7), ("\033[33mЖёлтый", 2), ("\033[32mЗелёный", 4))
        self.__index = 0

    def running(self):
        self.__index = 0

        for el in self.__all_colors:
            self.__change_state(el[0])
            time.sleep(el[1])

        print("\033[0mПрограмма завершенна.")

    def __change_state(self, color):
        self.__color = color
        print(f"\033[0mТекущий цвет: {self.__color}")


tf = TrafficLight()
tf.running()
