"""
4) Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""
mes = input("Введите строку из нескольких слов через пробелы ").split()
for i in range(len(mes)):
    print(f'{i} - {mes[i][:10]}')