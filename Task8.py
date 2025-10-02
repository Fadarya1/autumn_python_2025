
# todo: Проверить истинность высказывания: "Данное четырехзначное число
#  читается одинаково слева направо и справа налево".

four_digits = (input("Четырехзначное число: "))
if (four_digits[0] == four_digits[3]):
    if (four_digits[1] == four_digits[2]):
        print(bool(four_digits) == 1)
else:
    print(bool(four_digits) == 0)