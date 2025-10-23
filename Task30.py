# todo: Вы работаете с данными цен товаров, которые приходят в разном формате.
# Создайте список числовых значений цен,  игнорируя некорректные записи.
# Все цены переведите в рубли. Задачу следует решить с использованием списковых включений.
# from curses.ascii import isdigit

prices = ["₽1500", "20.50 USD", "invalid", "€25.00", "$15.99",  "18.99", "N/A", "¥5000"]
# corrections = [price.replace("USD", "$") for price in prices if "USD" in prices]
# print(corrections)
# correct_prices = [price for price in prices if price.startswith("$") or price.startswith("€")
#                   or price.startswith("¥") or price.startswith("₽") or price.endswith("USD")]
# print(correct_prices)
# for price in correct_prices:
#     x = price[0]
#     if x == "$":
#         price = float(price[1:]) * 80
#     if x == "€":
#         price = float(price[1:]) * 90
#     if x == "¥":
#         price = float(price[1:]) * 0.5387
#     if x == "₽":
#         price = float(price[1:])
    # print(price)

correct_prices_rubles = (([float(price[1:]) for price in prices if price.startswith("₽")]+
              [float(price[1:]) * 80 for price in prices if price.startswith("$")]+
              [float(price[1:]) * 90 for price in prices if price.startswith("€")]+
              [float(price[1:]) * 0.5387 for price in prices if price.startswith("¥")])+
              [float(price[:(price.index("USD"))])*80 for price in prices if price.endswith("USD")])

print(correct_prices_rubles)
# for price in prices:
#     if price.find("₽"):
#         for element in price:
#             if not element.isdigit() or not ".":
#
# print(prices)
# correct_prices = []
# new_array = [f'{element}' if element.isdigit else f'{element}-НЕТ' for price in prices for element in price ]


    # currency_and_price = [0, 0]

#         if element.isdigit() or element == ".":
#             currency_and_price[0] = "".join(element)
# print(correct_prices)
    # dict_prices = {key.isdigit(): str(value) for (key, value) in prices}

#     if "USD" or "$" in price:
#         currency_index = price.find("USD" or "$" or "¥" or "€" or "₽")
#     if "¥" in price:
#
#     if "€" in price:
#
#     if "₽" in price:
#         print(currency_index, price)

    # for element in price:

        # element.find("₽", isdigit)
        # element.find("$", isdigit)
        # element.find("€", isdigit)
        # element.find("¥", isdigit)
    # if "USD" or "$" in price:
    #     price = prices nonlocal price.replace("")
    # float(price)
# new_list_prices = []
# [new_list_prices.append(i) if float(i) is True else 0 for i in prices]
#
# print(new_list_prices)

# print(isalnum(prices[1]))
