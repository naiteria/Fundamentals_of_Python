from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_expense(self):
        pass


class Coat(Clothes):
    size: int

    def __init__(self, size: int):
        self.size = size

    @property
    def cloth_expense(self):
        a = round(((2 * self.size) + 0.3), 2)
        return f'Расход ткани на данное пальто составит: {a} метров.'


class Suit(Clothes):
    height: int

    def __init__(self, height: int):
        self.height = height

    @property
    def cloth_expense(self):
        a = round(((self.height / 6.5) + 0.5), 2)
        return f'Расход ткани на данный костюм составит: {a} метров.'


class TotalExpense(Clothes):
    size: int
    height: int

    def __init__(self, size: int, height: int):
        self.size = size
        self.height = height

    @property
    def cloth_expense(self):
        a = round(((2 * self.size + 0.3) + (self.height / 6.5 + 0.5)), 2)
        return f'Общий расход ткани составит: {a} метров.'


client1 = Coat(3)
print(client1.cloth_expense)

client2 = Suit(40)
print(client2.cloth_expense)

total = TotalExpense(3, 40)
print(total.cloth_expense)
