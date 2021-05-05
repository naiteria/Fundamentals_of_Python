while True:
    some_str = input('Пожалуйста, введите не менее трех слов разделяя их пробелами: ')
    if len(some_str) < 3 or some_str.count(' ') < 1:
        print('Неправильно введенные данные. Попробуйте еще раз')
        continue

    break

for i, word in enumerate(some_str.split()):
    print(i + 1, (word, word[:11])[len(word) > 10])
