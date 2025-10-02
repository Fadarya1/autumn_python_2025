#  todo: Дан номер месяца (1 — январь, 2 — февраль, ...).
#   Вывести название соответствующего времени года ("зима", "весна" и т.д.).
from unittest import case


# month = int(input("Введите номер месяца: "))
# if month == 12 or month == 1 or month == 2:
#     print("Зима!")
# elif month == 3 or month == 4 or month == 5:
#     print("Весна!")
# elif month == 6 or month == 7 or month == 8:
#     print("Лето!")
# elif month == 9 or month == 10 or month == 11:
#     print("Осень!")
# else:
#     print("Число должно быть от 1 до 12")
#     exit(1)

def get_season(month):
    match month:
        case 12 | 1 | 2:
            return "зима"
        case 3 | 4 | 5:
            return "весна"
        case 6 | 7 | 8:
            return "лето"
        case 9 | 10 | 11:
            return "осень"
        case _:
            return "Неверное число месяца"
month = int(input("Введите число месяца: "))
print(get_season(month))