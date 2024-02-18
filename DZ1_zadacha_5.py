# Anatoli Gutovski
# Date: 19/02/2024
# Description: Homework 2_zadacha_5
# Grodno IT Academy Python 3.11.7


# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.


def count_string_capitalization(mixed_string):
    # Cоздадим переменные для подсчета количества строчных и прописных букв
    lowercase_count = 0
    uppercase_count = 0

    # Пройдемся по каждому символу в строке
    for char in mixed_string:
        # Проверяем, является ли символ строчной буквой
        if char.islower():
            lowercase_count += 1
        # Проверяем, является ли символ прописной буквой
        elif char.isupper():
            uppercase_count += 1

    # Возвращаем количество строчных и прописных букв в виде кортежа
    return (lowercase_count, uppercase_count)


# Пример использования функции
input_string = "Hello World. Lets go BAMbinO"
result = count_string_capitalization(input_string)
print("Количество строчных букв:", result[0])
print("Количество прописных букв:", result[1])
