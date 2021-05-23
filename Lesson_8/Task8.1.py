class Date:
    date: str

    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_extraction(cls, date):
        user_date = date.replace('-', ' ').split()

        try:
            date_int_list = [int(number) for number in user_date]
            return date_int_list

        except ValueError:
            return f'Your input: {date}'

    @staticmethod
    def date_validation(extracted_date):
        try:
            the_date = '.'.join(str(x) for x in extracted_date)

            if extracted_date[0] <= 0 or extracted_date[0] >= 32:
                return f'\nYour date: {the_date}\nIncorrect day: {extracted_date[0]}'

            elif extracted_date[1] <= 0 or extracted_date[1] >= 13:
                return f'\nYour date: {the_date}\nIncorrect month: {extracted_date[1]}'

            elif extracted_date[2] <= 1920 or extracted_date[2] >= 2025:
                return f'\nYour date: {the_date}\nIncorrect year: {extracted_date[2]}'

            else:
                return f"\nYour date: {the_date}\nCorrect data information."

        except TypeError:
            return f'\n{extracted_date}\nIncorrect input'

    def __str__(self):
        return str(Date.date_validation(Date.date_extraction(self.date)))


my_date1 = Date('31-12-2021')
print(my_date1)

my_date1 = Date('1-31-1992')
print(my_date1)

my_date1 = Date('32 12 2085')
print(my_date1)

my_date1 = Date('12-12-02')
print(my_date1)

my_date1 = Date('12-some-02')
print(my_date1)
