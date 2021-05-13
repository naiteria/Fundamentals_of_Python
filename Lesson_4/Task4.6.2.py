from itertools import cycle

test_list = [1, 2, "что-то", True, 75.7]

c = 0
for el in cycle(test_list):
    if c > 30:
        break

    print(el)
    c += 1
