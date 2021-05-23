class ComplexNumber:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def __add__(self, other):
        return f'Сумма комплексных чисел: z = {self.first_number + other.first_number} + ' \
               f'{self.second_number + other.second_number} * i\n'

    def __mul__(self, other):
        return f'Умножение комплексных чисел: ' \
               f'z = {((self.first_number * self.second_number) - (other.first_number * other.second_number))} ' \
               f'+ {((other.first_number * self.second_number) + (self.first_number * other.second_number))} * i'

    def __str__(self):
        return f'Комплексное число: z = {self.first_number} + {self.second_number} * i\n'


first_complex_number = ComplexNumber(11, -12)
second_complex_number = ComplexNumber(13, 14)

print(first_complex_number)

print(first_complex_number + second_complex_number)

print(first_complex_number * second_complex_number)
