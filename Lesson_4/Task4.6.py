from itertools import count

start_number = int(input("Введите стартовое число: "))
end_number = int(input("Введите последнее число: "))

for el in count(start_number):
    if el > end_number:
        break

    print(el)
