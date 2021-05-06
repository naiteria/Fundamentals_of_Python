def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


def my_func_use():
    print(my_func((int(input('Введите первое число: '))), (int(input('Введите второе число: '))),
                  (int(input('Введите третье число: ')))))


my_func_use()
