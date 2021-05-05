seasons_list = [
    ['Зима', ['12', '1', '2']],
    ['Весна', ['3', '4', '5']],
    ['Лето', ['6', '7', '8']],
    ['Осень', ['9', '10', '11']]
]

seasons_dict = {
    'Зима': ['12', '1', '2'],
    'Весна': ['3', '4', '5'],
    'Лето': ['6', '7', '8'],
    'Осень': ['9', '10', '11']
}

while True:
    month_number = input('Пожалуйста, введите номер месяца, а программа отпределит сезон: ')
    if month_number not in sum(seasons_dict.values(), []):
        print('Неправильно введенный номер месяца. Попробуйте еще раз. Напомню, в году 12 месяцев.')
        continue
    break

for season, months in seasons_list:
    if month_number in months:
        print(f'Список моих сезонов определил, что {month_number}-й месяц — это {season}.')

for season, months in seasons_dict.items():
    if month_number in months:
        print(f'Словарь моих сезонов определил, что {month_number}-й месяц — это {season}.')
