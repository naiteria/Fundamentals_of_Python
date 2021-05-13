from functools import reduce
from random import randrange


def task5():
    rand_list = [randrange(100, 1001, 2) for _ in range(randrange(5, 21))]
    print(f"Произвольный список от 5 до 20 элементов, каждый элемент которого является случайным "
          f"чётным числом в диапазоне от 100 до 1000:\n{rand_list}\n")
    print(f"В результате произведения всех элементов списка получено следующее число:\n"
          f"{reduce(lambda prev_el, el: prev_el * el, rand_list)}\n")


task5()
