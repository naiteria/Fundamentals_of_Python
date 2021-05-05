products, order = [], 1
title, price, amount = None, None, None

while True:
    if title is None:
        tmp = input('Введите название товара: ')
        if not tmp.isalnum():
            print('Наименование товара не может быть пустым. Попробуйте еще раз.')
            continue

        title = tmp

    if price is None:
        tmp = input('Введите стоимость товара: ')
        if not tmp.isdigit():
            print('Цена должна быть целым числомю. Попробуйте еще раз.')
            continue

        price = int(tmp)

    if amount is None:
        tmp = input('Введите количество: ')
        if not tmp.isdigit():
            print('Количество должно быть целым числом. Попробуйте еще раз.')
            continue

        amount = int(tmp)

    tmp = input('Введите единицы измерения: ')
    if not tmp.isalpha():
        print('Единица изменерения не может быть пустой. Попробуйте еще раз.')
        continue

    unit = tmp

    products.append((
        order,
        {
            'Наименование': title,
            'Цена': price,
            'Количество': amount,
            'Единица измерения': unit
        }
    ))

    title, price, amount = None, None, None
    order += 1

    print(products)

    q = input('Формирование списка завершено? (y/N)) ')
    if q.lower() == 'y':
        break

summary = {
    'title': [],
    'price': [],
    'amount': [],
    'unit': set()
}

for _, item in products:
    summary['title'].append(item['title'])
    summary['price'].append(item['price'])
    summary['amount'].append(item['amount'])
    summary['unit'].add(item['unit'])

print(summary)
