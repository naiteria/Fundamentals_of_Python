class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self.__color = color
        self._name = name
        self.__is_police = is_police

    def go(self):
        print(f"[{self._name}]: Машина отправилась в путь")
        self.__print_car_info()

    def stop(self):
        print(f"[{self._name}]: Машина остановилась")

    def turn(self, direction):
        print(f"[{self._name}]: Машина изменила направление. Текущее значение: {direction}")

    def show_speed(self):
        print(f"[{self._name}]: Скорость: {self._speed}")

    def __print_car_info(self):
        print(f"[{self._name}]: Цвет - {self.__color}, текущая скорость - {self._speed}, полицейская машина? "
              f"- {self.__is_police}")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()

        if self._speed > 60:
            print(f"[{self._name}]: Обнаружено превышение скорости!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        super().show_speed()

        if self._speed > 40:
            print(f"[{self._name}]: Обнаружено превышение скорости!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


# TownCar
tc = TownCar(40, "Мокрый асфальт", "Lada")
tc.go()
tc.turn("Лево")
tc.show_speed()
tc.stop()

tc = TownCar(64, "Черный", "Mercedes")
tc.go()
tc.show_speed()
tc.stop()

# SportCar
sc = SportCar(150, "Желтый", "Lamborghini")
sc.go()
sc.show_speed()
sc.stop()

# WorkCar
wc = WorkCar(20, "Зелебристый", "Opel")
wc.go()
wc.show_speed()
wc.turn("Северо-восток")
wc.stop()

wc = WorkCar(89, "Чёрный", "Citroen")
wc.go()
wc.show_speed()
wc.stop()

# PoliceCar
pc = PoliceCar(120, "Белый", "Skoda")
pc.go()
pc.show_speed()
pc.turn("Назад")
pc.stop()
