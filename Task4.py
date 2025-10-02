# todo: Заданы три числа в переменных x, y, z.
# Напечатать наибольшее из этих чисел.
# Пример:
# x = 10
# y = 15
# z = 2
# Ответ:
# Наибольшее число 15

# Пример:
# x = 77
# y = 9
# z = 130
# Ответ:
# Наибольшее число 130

# Задачу решить без функций max и прочих.
# Значение переменных может меняться
#
x = int(input("Число X: "))
y = int(input("Число Y: "))
z = int(input("Число Z: "))
#
# if (x > y):
#     big = x
# else:
#     big = y
# if(z > big):
#     print("Наибольшее число: ", z)
# else:
#     print("Наибольшее число: ", big)
maximum_number = x if x > y else y
maximum_number = maximum_number if maximum_number > z else z
print("Самое большое число: ", maximum_number)