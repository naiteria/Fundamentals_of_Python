def salary():
    try:
        time = float(input('Выработка в часах: '))
        wages = float(input('Ставка в у.е.: '))
        bonus = float(input('Премия в у.е.: '))
        result = time * wages + bonus
        print(f'Заработная плата сотрудника: {result}')
    except ValueError:
        return print('Not a number')


salary()
