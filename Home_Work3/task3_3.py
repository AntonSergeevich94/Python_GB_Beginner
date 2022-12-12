"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(arg1, arg2, arg3):
    """Функция находит минимальное из 3х чисел и вычитает его из общей суммы"""
    min_arg = arg1
    if arg2 < min_arg:
        min_arg = arg2
    if arg3 < min_arg:
        min_arg = arg3
    return arg1 + arg2 + arg3 - min_arg


print(my_func(100000, -10, 10))
