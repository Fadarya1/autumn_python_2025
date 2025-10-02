# todo: Написать программу, которая считывает два числа и выводит их сумму,
# разность, частное, произведение,
# результат целочисленного деления, результат деления с остатком,
# результат возведения в степень.

Number1 = int(input("Первое число: "))
Number2 = int(input("Второе число: "))
Summ = Number1 + Number2
print("Результат суммы: ", Summ)
Deduction = Number1 - Number2
print("Результат разности: ", Deduction)
Division = Number1 / Number2
print("Результат целочисленного деления: ", int(Division))
print("Результат деления с остатком: ", Division)
Multiplication = Number1 * Number2
print("Результат произведения: ", Multiplication)
Exponention = Number1 ** Number2
print("Результат возведения в степень: ", Exponention)