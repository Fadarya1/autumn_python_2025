#todo: Даны три точки A , B , C на числовой оси. Найти длины отрезков AC и BC
# и их сумму.
# Примечание: все точки получаем через функцию input().

A = int(input("Число А: "))
B = int(input("Число B: "))
C = int(input("Число C: "))
if (A > C):
    AC = A - C
else:
    AC = C - A
print("Длина отрезка АС: ", AC)
if (B > C):
    BC = B - C
else:
    BC = C - B
print("Длина отрезка ВС: ", BC)
print("Сумма отрезков = ", AC + BC)