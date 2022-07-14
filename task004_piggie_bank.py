x, p, y = map(int, input('Введи размер вклада, процентную ставку и желаемую сумму: ').split())
years = 0
while x < y:
    x = x + (x * p / 100)
    years += 1
print(f'Желаемая сумма будет через {years} лет')