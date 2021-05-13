numbers_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

new_list = []

with open('Task5.4.txt', encoding='utf-8') as text:
    [new_list.append(f'{numbers_dict[i.split()[0]]} {i.split()[1]} {i.split()[2]}') for i in text]

with open('new_task5.4.txt', 'w') as new_text:
    [print(i, file=new_text) for i in new_list]
