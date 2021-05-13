import json


def short_info(info_list):
    dicts_list = []
    companies_profit_dict = {}
    companies_loss_dict = {}
    average_profit_dict = {}
    order_counter = 0
    company_counter = 0
    total_profit = 0
    print('\nКраткая справка по компаниям:')
    for i in info_list:
        if (int(i[2]) - int(i[3])) > 0:
            order_counter += 1
            company_counter += 1
            companies_profit_dict[i[0]] = (int(i[2]) - int(i[3]))
            print(f'{order_counter}) Прибыль компании "{i[0]}" составляет: {(int(i[2]) - int(i[3]))} рублей.')
            total_profit += (int(i[2]) - int(i[3]))
        else:
            order_counter += 1
            companies_loss_dict[i[0]] = (int(i[2]) - int(i[3]))
            print(f'{order_counter}) Компания "{i[0]}" работает в убыток.')
    print(f'\nСредняя прибыль по компаниям: {round((total_profit / company_counter), 2)}\n')
    average_profit_dict['average_profit'] = round((total_profit / company_counter), 2)

    dicts_list.append(companies_profit_dict)
    dicts_list.append(companies_loss_dict)
    dicts_list.append(average_profit_dict)

    return dicts_list


with open('Task5.7.txt', encoding='utf-8') as text:
    my_list = [line.split() for line in text]
    with open('Task5.7.json', 'w') as json_file:
        json.dump(short_info(my_list), json_file, indent=4, ensure_ascii=False)
