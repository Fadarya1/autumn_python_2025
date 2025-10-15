# #todo:  Задан файл dump.txt. Необходимо для заданного файла подсчитать статистику количества
# # гласных букв в тексте.
#
# #Формат вывода:
# Количество букв a - 13
# Количество букв o - 12
# Количество букв e - 11

f=open("dump.txt","rt", encoding="utf-8")
vowels = ['а', 'е', 'и', 'о', 'у', 'ю', 'я', 'э', 'ё', 'ы']
# indexes = list()
# for letter in vowels:
#     indexes.append(ord(letter))
# print(indexes)
count = [0] * 10
i = 0
for line in f:#18 букв А
    for index_number in range(len(vowels)):
        for letter in line:
             if vowels[index_number] == letter or vowels[index_number] == letter.lower():
                 count[index_number] = count[index_number] + 1
             if letter not in line:
                 count[index_number] = 0
    i += 1

for a in range(len(vowels)):
    print(f"Количество букв {vowels[a]} - {count[a]}")
f.close()
