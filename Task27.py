# #todo: Числа в буквы
# Замените числа, написанные через пробел, на буквы. Не числа не изменять.
#
# Пример.
# Input	                            Output
# 8 5 12 12 15	                    hello
# 8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
abc = list()
i = 0
for i in range(26):
    abc.append(chr(ord("a")+i))
user_input = str(input("Enter your input: "))
user_input = user_input.split(" ")
user_output = list()
for element in user_input:
    if element.isdigit():
        if element == "0":
            user_output.append(" ")
        else:
            user_output.append((abc[int(element) - 1]))
    else:
        user_output.append(element)
x = "".join(user_output)
print(x)