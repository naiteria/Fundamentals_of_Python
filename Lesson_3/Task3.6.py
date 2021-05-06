def int_func(word):
    if all([96 < ord(char) < 123 for char in word]):
        return chr(ord(word[0]) - 32) + word[1:]


while True:
    user_input = input("Введите слова из латинских букв в нижнем регистре, разделенные пробелами: ").split()
    new_list = list(map(int_func, user_input))
    if all([word is not None for word in new_list]):
        print(f"Новое предложение: {' '.join(new_list)}")
