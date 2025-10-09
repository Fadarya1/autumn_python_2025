#  Дан массив размера N. Найти минимальное растояние между одинаковыми
#  значениями в массиве и вывести их индексы.
# # Одинаковых значение может быть два и более !
# Пример:
# mass = [1,2,17,54,30,89,2,1,6,2]
#
# Для числа 1 минимальное растояние в массиве по индексам: 0 и 7
# Для числа 2 минимальное растояние в массиве по индексам: 6 и 9
# Для числа 17 нет минимального растояния т.к элемент в массиве один.

import random

def asking_for_array(): #Функция создает list чисел
    get_a_mass = list()
    ask_for_array = int(input("Хотите создать массив автоматически? 1 - да, 2 - нет "))
    if ask_for_array == 1:
        number_of_elements = int(input("Сколько элементов в массиве? "))
        get_a_mass = [0] * number_of_elements
        for i in range(number_of_elements):
            get_a_mass[i] = random.randint(1, 100)
    elif ask_for_array == 2:
        get_a_mass = list(map (int, input("Введите массив: ").split()))
    print(get_a_mass)
    return get_a_mass

get_a_mass = asking_for_array()
dict_quantity = {}
dict_index_of_number = {}
def if_count_is_bigger(needed_number):
    #функция находит наименьшее расстояние между индексами, если число повторяется в list 2 и больше раз
    index_of_numbers = []
    for number in get_a_mass:
        if number == needed_number:
            index_of_numbers.append(get_a_mass.index(number))
            get_a_mass.insert(get_a_mass.index(number), 0)
            get_a_mass.remove(number)
    order_number = 0
    minimum_space = len(get_a_mass)
    minimum_space_indexes = list()
    for x in range (len(index_of_numbers) - 1):
        if (abs(index_of_numbers[order_number] - index_of_numbers[order_number+1])) < minimum_space:
            minimum_space = abs(index_of_numbers[order_number] - index_of_numbers[order_number+1])
            minimum_space_indexes = [index_of_numbers[order_number], index_of_numbers[order_number+1]]
        order_number += 1
    return minimum_space_indexes

for number_ in get_a_mass:
    dict_quantity[number_] = get_a_mass.count(number_)
    #key - число из главного списка, value - количество этих чисел в списке
    dict_index_of_number[number_] = get_a_mass.index(number_)
    match get_a_mass.count(number_):
        case 1:
            print(f"Для числа {number_} нет минимального расстояния, так как элемент в массиве один")
        case _:
            if number_ != 0:
                print(f"Для числа {number_} минимальное расстояние по индексам: {if_count_is_bigger(number_)}")
    continue
#     if get_a_mass.count(number_) > 1:
#         for index_number_ in get_a_mass:
#             if get_a_mass[index_number_] == dict_index[number_]:
#                 dict_index_of_numbers[index_number_] = get_a_mass[index_number_]
# print(dict_index_of_numbers)
#
#
#
# print(dict_index)
# exit()
# for i in range(number_of_elements):
#
#     if get_a_mass.count(number_) > 1:
#         j = 0
#         while j < get_a_mass.count(number_):
#             dict_index_of_numbers[number_][j] = get_a_mass.index(number_)
#             j += 1
# print(len(dict_index))
# exit()
# print(dict_index_of_numbers)
#     written_indexes = list([0])
#     for i in range(len(dict_index)):
#         if dict_index.keys == 1:
#             print(f"Для числа {dict_index.values} нет минимального расстояния, так как элемент в массиве один")
#         else:
#             for element in get_a_mass:
#                 written_indexes = written_indexes * get_a_mass.count(element)
#                 for index_ in range(len(written_indexes)):
#                     written_indexes[index_] = get_a_mass.index(element)
#
#                 print(written_indexes)
#                 exit()
# decide()
# if dict_index:
# different_elements = tuple(set(get_a_mass))
# print(different_elements)
# array_of_indexes = list()
# length_de = len(different_elements)
# print(length_de)
# for i in range(length_de):
#     for j in range(number_of_elements):
#         # if get_a_mass[j] == different_elements[i]: #сравнить
#         #     print(get_a_mass.index(get_a_mass[i]))
#         #     length_of_index = get_a_mass.count(int(tuple(different_elements)[j]))
#         #     print(get_a_mass.count(int(str(different_elements)[j])))
#         array_of_indexes[i] = get_a_mass.count(different_elements[j])
#         print(array_of_indexes[i])

# numbers_used_not_once = (get_an_array - different_elements)
# print(numbers_used_not_once)
# for i in different_elements:
#     print(i)
    # for number in range (1, amount):
    #     index_of_numbers = index_of_numbers * number
    #     print(index_of_numbers)
    # index_of_numbers = index_of_numbers * amount
    # print(index_of_numbers)
    # for i in range(len(get_a_mass)):
    #     for j in range(len(dict_quantity)):
    #         if get_a_mass[i] == dict_quantity.keys[j]:
    #             for k in range(get_a_mass.count(i)):
    #
    #                     = set(dict_quantity[get_a_mass[i]])
    # return -1