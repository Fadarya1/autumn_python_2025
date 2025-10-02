# В восточном календаре принят 60-летний цикл, состоящий из 12- летних подциклов,
# обозначаемых названиями цвета: зеленый, красный, желтый, белый и черный.
# В каждом подцикле годы носят названия животных: крысы, коровы, тигра, зайца, дракона,
# змеи, лошади, овцы, обезьяны, курицы, собаки и свиньи.
# По номеру года вывести его название,
# если 1984 год был началом цикла — годом зеленой крысы.

year = int(input("Введите год: "))
animal = ("крыса", "бык", "тигр", "кролик", "дракон", "змея",
          "лошадь", "коза", "обезьяна", "петух", "собака", "свинья")
color = ("green", "red", "yellow", "white", "black")
print(color[(year-1984) % 5], animal[(year - 1984) % 12])

# color = ["green", "red", "yellow", "white", "black"]
# # print(color[1])
# animal = ["Крыса", "Корова", "Тигр", "Заяц", "Дракон",
#         "Змея", "Лошадь", "Овца", "Обезьяна","Курица", "Собака", "Свинья"]
# print(animal[3])
# def get_color(year):
#     match year:
#         case year if 1984 <= year < 1996:
#             return "green"
#         case year if 1996 <= year < 2008:
#             return "red"
#         case year if 2008 <= year < 2020:
#             return "yellow"
#         case year if 2020 <= year < 2032:
#             return "white"
#         case year if 2032 <= year < 2044:
#             return "black"
# def get_animal(year):
#     if year in range(1984, 2104, 12):
#         return "крыса"
#     elif year in range(1985, 2104, 12):
#         return "корова"
#     elif year in range(1986, 2104, 12):
#         return "тигр"
#     elif year in range(1987, 2104, 12):
#         return "заяц"
#     elif year in range(1988, 2104, 12):
#         return "дракон"
#     elif year in range(1989, 2104, 12):
#         return "змея"
#     elif year in range(1990, 2104, 12):
#         return "лошадь"
#     elif year in range(1991, 2104, 12):
#         return "овца"
#     elif year in range(1992, 2104, 12):
#         return "обезьяна"
#     elif year in range(1993, 2104, 12):
#         return "курица"
#     elif year in range(1994, 2104, 12):
#         return "собака"
#     elif year in range(1995, 2104, 12):
#         return "свинья"
# year = int(input("Введите год: "))
# print(get_color(year), get_animal(year))
#
# color = ["green", "red", "yellow", "white", "black"]
# for year in range (1984, 10000):
#     for i = 0,
#     match year:
#         case color[i]
#
