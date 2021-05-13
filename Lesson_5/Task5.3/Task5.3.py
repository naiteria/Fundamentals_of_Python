with open('Task5.3.txt', encoding='utf-8') as text:
    users_list = []
    employee_number = 0
    less_twenty = 0
    print('\nСписок сотрудников, с заработной платой меньше 20000 рублей:')
    for i in text:
        users_list.append(float(i.split()[1]))
        employee_number += 1
        if float(i.split()[1]) < 20000:
            less_twenty += 1
            print(f'{less_twenty}) {i.split()[0]}, {i.split()[1]} рублей')

    print(f'\nСредняя величина дохода сотрудников составляет: {round((sum(users_list) / employee_number), 2)} рублей.')
