# #todo: Выведите все строки данного файла в обратном порядке, допишите их в этот же файл.
# # Для этого считайте список всех строк при помощи метода readlines().
# #
# # #Содержимое файла inverted_sort.txt
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# #
# # Результат
# Complex is better than complicated.
# Simple is better than complex.
# Explicit is better than implicit.
# Beautiful is better than ugly.

inverted = open("inverted_sort.txt", "wt")
inverted.write("Beautiful is better than ugly.\n")
inverted.write("Explicit is better than implicit.\n")
inverted.write("Simple is better than complex.\n")
inverted.write("Complex is better than complicated.\n")
inverted.write("\n")
inverted.close()

inverted = open("inverted_sort.txt", "r+")
object = inverted.readlines()
object.reverse()
inverted.writelines(object)
# print(object)
# print(f"{object[0]}")
# inverted.writelines(object)
# for x in range(len(object)):
#     inverted.write(f"{object[x]}")
inverted.close()
# uninverted = list()
# length_ = len(inverted.readlines())
#
# for i in range(length_):
#     uninverted.append(inverted.readlines())
#     uninverted[i] = inverted.readlines[length_]
#     inverted.write(uninverted[i])
#     length_ =- 1
inverted.close()