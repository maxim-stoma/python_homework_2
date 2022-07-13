number = int(input('Факториал какого числа будем искать? '))
factorial = 1
for i in range(2, number + 1):
    factorial *= i
print(f'Факториалом числа {number} является {factorial}.')