import random
array = (random.sample(range(99), 10))
array.append(0)
print(f'Исходный массив {array}')
sorted_array = sorted(array, reverse=True)
print(f'Второй по величине элемент массива: {sorted_array[1]}')