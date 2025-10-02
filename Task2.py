# # todo: Преобразуйте переменную age и foo в число
#
age = int("23")
print("age is: ", type(age))
foo = "23abc" #ValueError: invalid literal for int() with base 10: '23abc'
print("foo is: ", type(foo))

# Преобразуйте переменную age в Boolean
age = bool("123abc")
print("age is: ", type(age))
#
# Преобразуйте переменную flag в Boolean
flag = bool(1)
print("flag is: ", type(flag))
print(bool(flag)) #true
# Преобразуйте значение в Boolean
str_one = bool("Privet")
print("str_one is: ", type(str_one))
print(bool(str_one)) #true
str_two = bool("")
print("str_two is: ", type(str_two))
print(bool(str_two)) #false
# Преобразуйте значение 0 и 1 в Boolean
print(bool(1)) #true
print(bool(0)) #false

# Преобразуйте False в строку
str_f = "False"
print("str_f is: ", type(str_f))