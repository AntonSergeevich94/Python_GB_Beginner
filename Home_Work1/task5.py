"""
5) Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма (прибыль — выручка
больше издержек, или убыток — издержки больше выручки). Выведите
соответствующее сообщение. Если фирма отработала с прибылью, вычислите
рентабельность выручки (соотношение прибыли к выручке). Далее запросите
численность сотрудников фирмы и определите прибыль фирмы
 в расчете на одного сотрудника.
"""
earn = int(input("Введите значение выручки фирмы "))
cost = int(input("Введите значение издержек фирмы "))
if earn > cost:
    print("Финансовый результат работы - ПРИБЫЛЬ")
    print(f"Рентабельность выручки {(earn - cost) * 100 / earn} %")
    people = int(input("Ведите численность сотрудников "))
    print(f"Прибыль на одного сотрудника {(earn - cost) / people}")
else:
    print("Финансовый результат работы - УБЫТОК")