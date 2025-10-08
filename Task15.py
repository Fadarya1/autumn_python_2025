#Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.

import random
array_of_numbers = [0] * 10
new_array_of_numbers = array_of_numbers[:]
i = 0
while i < 10:
    number = random.randint(1, 1000)
    new_number = number + 1
    array_of_numbers[i] = number
    new_array_of_numbers[i] = new_number
    i += 1
print(f"Целочисленный массив: {array_of_numbers}")
print(f"Новый массив: {new_array_of_numbers}")