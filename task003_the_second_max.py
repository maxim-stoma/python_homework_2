import random
array = (random.sample(range(99), 10))
array.append(0)
print(f'Исходный массив {array}')
sorted_array = sorted(array, reverse=True)
second_max = sorted_array[1]
for i in range(len(sorted_array)):
    if sorted_array[0] == sorted_array[i]:
        second_max = sorted_array[i + 1]
print(f'Второй по величине элемент массива: {second_max}')