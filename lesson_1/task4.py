n = int(input('Введите целое положительное число, а программа найдет самую большую цифру в этом числе: '))
max: int = n % 10

while n >= 0:
    n = n // 10
    if n % 10 > max:
        max: int = n % 10
    elif n > 9:
        continue
    else:
        print('Максимальное цифра в числе: ', max)
        break
