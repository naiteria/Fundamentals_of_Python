class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self, weight_1cm, thickness):
        return self._length * self._width * weight_1cm * thickness


road = Road(int(input('Введите ширину дороги в метрах: ')), int(input('Введите длину дороги в метрах: ')))
var_1 = (road.calc_weight(25, 5))
var_2 = road.calc_weight(25, 10)

print(f'При толщине 5 см потребуется {var_1} кг асфальта.')
print(f'При толщине 10 см потребуется {var_2} кг асфальта.')
