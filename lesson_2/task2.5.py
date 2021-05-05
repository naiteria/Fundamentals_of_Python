number = int(input("Пожалуйста, введите число: "))
my_list = [7, 5, 3, 3, 2]
a = my_list.count(number)
for element in my_list:
    if a > 0:
        i = my_list.index(number)
        my_list.insert(i + a, number)
        break
    else:
        if number > element:
            b = my_list.index(element)
            my_list.insert(b, number)
            break
        elif number < my_list[len(my_list) - 1]:
            my_list.append(number)
print(my_list)
