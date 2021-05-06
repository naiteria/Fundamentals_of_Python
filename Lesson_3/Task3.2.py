def user_data(**kwargs):
    return list(kwargs.values())


def user_data_use():
    print(user_data(name=input('Введите Ваше имя: '),
                    sure_name=input('Введите Вашу фамилию: '),
                    birth_date=input('Укажите дату Вашего рождения: '),
                    live_town=input('В каком городе Вы проживаете? '),
                    email=input('Укажите адрес электронной почты: '),
                    tel=input('Укажите контактный номер телефона: ')))


user_data_use()
