# # todo: Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм,
# #  3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы и масса тела M
# #  в этих единицах (вещественное число).
# #  Вывести массу данного тела в килограммах
#
# type = int(input("Введите код единицы массы: "))
# if type < 1 or type > 5:
#     print("Введите код от 1 до 5")
#     exit(1)
# weight = float(input("Введите вес тела: "))
# if type == 1:
#     print("Вес тела: ", weight, "кг")
# elif type == 2:
#     print("Вес тела: ", weight / 1000000, "кг")
# elif type == 3:
#     print("Вес тела: ", weight / 1000, "кг")
# elif type == 4:
#     print("Вес тела: ", weight * 1000, "кг")
# elif type == 5:
#     print("Вес тела: ", weight * 100, "кг")
#




TYPE = list(range(1,6))
print(TYPE)

def collect_data():
    #Эта функция собирает информацию от пользователя
    type = int(input("Введите код единицы массы: "))
    if type not in TYPE:
        print("Ошибка: Введите код от 1 до 5")
        exit(1)
    weight = float(input("Введите вес тела: "))
    return type, weight
def convert_weight():
    #Эта функция конвертирует вес в килограммы
    type, weight = collect_data()
    if type == 1: weight = weight
    elif type == 2: weight = weight / 1000000
    elif type == 3: weight = weight / 1000
    elif type == 4: weight = weight * 1000
    elif type == 5: weight = weight * 100
    return weight
print("Вес тела: ", convert_weight(), "кг")