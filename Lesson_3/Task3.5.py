special_char = "q"


def get_numbers():
    """
    Запрашивает строку чисел у пользователя и возвращает сумму введенных чисел и флаг выхода
    """
    while True:
        user_input = input('Введите строку чисел, разделенных пробелом (q для выхода): ').split()

        flag = special_char in user_input
        index = user_input.index(special_char) if flag else len(user_input)

        try:
            return list(map(int, user_input[:index])), flag
        except ValueError:
            print('Это не список чисел!')


list_sum = 0

while True:
    num_list, exit_flag = get_numbers()
    list_sum += sum(num_list)
    print(f'Новая сумма: {list_sum}')
    if exit_flag:
        break
