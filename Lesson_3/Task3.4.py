def my_func(x, y):
    return 1 / x ** abs(y)


def my_func_use():
    print(my_func(2, -2))


def my_func_v2(x, y):
    for i in range(abs(y - 1)):
        x *= x
    return 1 / x


def my_func_v2_use():
    print(my_func(2, -2))


my_func_use()
my_func_v2_use()
