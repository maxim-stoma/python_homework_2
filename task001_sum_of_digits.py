number = "".join(input("Введи вещественное число (ну, это типа дробных) ").split("."))
print(f'Сумма цифр введённого числа равна {sum([int(i) for i in number])}')