class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


stationery = Stationery('канцелярская принадлежность')
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
