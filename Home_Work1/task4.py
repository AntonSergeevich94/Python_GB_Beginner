"""
4) Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл
while и арифметические операции.
"""
n = int(input("Введите целое положительное число "))
max_num = n % 10
while n > 0:
    if max_num < n % 10:
        max_num = n % 10
    n = n // 10
print(f"Самая большая цифра в числе {max_num}")
