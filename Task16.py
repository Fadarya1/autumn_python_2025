# База данных пользователя.
# Задан массив объектов пользователя
from unittest import case
users = [{'login': 'Piter', 'age': 23, 'group': "admin"},
         {'login': 'Ivan',  'age': 10, 'group': "guest"},
         {'login': 'Dasha', 'age': 30, 'group': "master"},
         {'login': 'Fedor', 'age': 13, 'group': "guest"}]
         # {'login': 'Juan', 'age': 20, 'group': "guest"},
         # {'login': 'Sava', 'age': 20, 'group': "master"},
         # {'login': 'Juannna', 'age': 20, 'group': "guest"},
         # {'login': 'Savan', 'age': 11, 'group': "guest"},
         # {'login': 'Diana', 'age': 12, 'group': "guest"},
         # {'login': 'Deona', 'age': 20, 'group': "master"},]

# Написать фильтр который будет выводить отсортированные объекты по возрасту
# (больше введеного),первой букве логина, и заданной группе.

# #Сперва вводится тип сортировки:
# 1. По возрасту
# 2. По первой букве
# 3. По группе
#
# тип сортировки: 1

number_of_users = len(users)
get_number_of_sort = int(input("Введите число от 1 до 3: "))
users_left = []
def get_needed_users_by_age():
    j = 0
    get_age = int(input("Пользователей старше какого возраста надо найти: "))
    for i in range(number_of_users):
        if (users[i]["age"]) > get_age:
            users_left.append(j)
            users_left[j] = users[i]
            j += 1
            continue
    users_left_sorted = sorted([(x['age'], x["login"], x["group"]) for x in users_left])
    for k in range(len(users_left_sorted)):
        print(f"Пользователь: {users_left_sorted[k][1]}, возраст: {users_left_sorted[k][0]}, группа: {users_left_sorted[k][2]}")
    exit()
def get_needed_users_by_login():
    j = 0
    get_a_letter = str.upper(input("Введите первую букву логина: "))
    count = 0
    for i in range(number_of_users):
        if users[i]['login'][0] == get_a_letter:
            count += 1
            users_left.append(users[i])
            users_left[j] = users[i]
            j += 1
            continue
    if count == 0:
        print("Пользователь не найден")
        exit()
    users_left_sorted = sorted([(x["login"], x["age"], x["group"]) for x in users_left])
    for k in range(len(users_left_sorted)):
        print(f"Пользователь: {users_left_sorted[k][0]}, возраст: {users_left_sorted[k][1]}, группа: {users_left_sorted[k][2]}")
        exit()

def get_needed_users_by_group():
    j = 0
    count_group = 0
    get_a_group_name = str.lower(input("Введите имя группы: "))
    for i in range(number_of_users):
        if users[i]['group'] == get_a_group_name:
            count_group += 1
            users_left.append(users[j])
            users_left[j] = users[i]
            j += 1
            continue
    users_left_sorted = sorted([(x["group"], x["login"], x["age"]) for x in users_left])
    if count_group == 0:
        print("Такой группы нет")
        exit()
    for k in range(len(users_left_sorted)):
        print(f"Пользователь: {users_left_sorted[k][1]}, "
              f"возраст: {users_left_sorted[k][2]}, "
              f"группа: {users_left_sorted[k][0]}")
    exit()

def sort_system():
    match get_number_of_sort:
        case 1: # 1. По возрасту
            return print(get_needed_users_by_age())
        case 2: # 2. По первой букве
            return print(get_needed_users_by_login())
        case 3: # 3. По группе
            return print(get_needed_users_by_group())
        case _:
            return "Число не в рамках интервала"
sort_system()

# i = 0
# for i in sorted_list:
#     print(users[i])
#     exit()
#     for key, val in users[dict[i]].items():
#         print(key, val)
#     i += 1

# items = sorted_list_of_users.items()
# for key in sorted(sorted_list_of_users):
#     print(key)
#
# #Затем сообщение для ввода
# Ввeдите критерии поиска: 16
# Результат:
# #Пользователь: 'Piter' возраст 23 года , группа  "admin"
# #Пользователь: 'Dasha' возраст 30 лет , группа  "master"