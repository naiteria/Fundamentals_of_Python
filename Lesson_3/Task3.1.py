def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    except ValueError:
        return 'Некорректные данные'


def division_use():
    print(division((int(input('Введите первое число: '))), (int(input('Введите второе число: ')))))


division_use()
