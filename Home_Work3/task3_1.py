"""
1)	Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.
"""


def divide_two_numbers(arg_1, arg_2):
    """Функция возвращает результат деления первого числа на второе"""
    return arg_1 / arg_2


a = float(input("Введите первое число  "))
b = float(input("Введите второе число  "))
if b == 0:
    print("На ноль делить нельзя!")
else:
    print(divide_two_numbers(a, b))