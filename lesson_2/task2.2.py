some_list = []

while True:
    item = input('Пожалуйста, введите элемент списка: ')
    some_list.append(item)

    question = input('Формирование списка завершено? (y/N)) ')
    if question.lower() == 'y':
        break

last_index = len(some_list) - 1

for index, _ in enumerate(some_list):
    if index % 2 == 0 and index < last_index:
        some_list[index + 1], some_list[index] = some_list[index:index + 2]

print(some_list)
