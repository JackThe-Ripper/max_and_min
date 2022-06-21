# Задачи на закрепление типов аргументов:
# Написать функцию, которая принимает любое количество аргументов чисел.
# Среди них она находит максимальное и минимальное. И возвращает оба

def max_and_min(*num):
    for item in num:
        item = max(num)
    for item1 in num:
        item1 = min(num)
    print('Max item is ', item, 'Min item is ', item1)
