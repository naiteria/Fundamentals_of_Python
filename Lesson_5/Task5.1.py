with open('my.txt', 'w') as text:
    while True:
        user_text = input('Введите любое значение для записи его в файл: ')
        if user_text == '':
            print('Вы вышли из программы!')
            break
        else:
            text.write(f'{user_text}\n')
            print('Для выхода оставьте строку пустой и нажмите клавишу "Enter".')
