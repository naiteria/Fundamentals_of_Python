try:
    numbers_list = list(map(int, input('Введите любое количество чисел через пробел: ').split()))
    with open('Task5.5.txt', 'w') as numbers:
        numbers.writelines(' '.join([str(number) for number in numbers_list]))
    with open('Task5.5.txt') as numbers_sum:
        my_numbers = [int(i) for i in [line.split() for line in numbers_sum][0]]
        print(f'Сумма введенных чисел: {sum(my_numbers)}.')
except ValueError:
    print('Введено некорректное значение!')
