class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname} ({self.position})"

    def get_total_income(self):
        income = self._income
        return income.get("wage") + income.get("bonus")


p = Position("Светлана", "Сальникова", "Универсальный продавец", {"wage": 51000, "bonus": 7000})
print(p.get_full_name())
print(p.get_total_income())

p = Position("Алёна", "Токорева", "Продавец", {"wage": 47000, "bonus": 5000})
print(p.get_full_name())
print(p.get_total_income())
