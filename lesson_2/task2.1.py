some_list = [79, -25.4, 'False', False, 'None', 246]


def some_type(i):
    for i in range(len(some_list)):
        print(type(some_list[i]))
    return


some_type(some_list)
