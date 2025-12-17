#todo: Реализовать декоратор в котором нужно подсчитать кол-во вызовов декорированной функции в процессе выполнения кода.
# Выгрузить статистику подсчета в файл debug.log в формате: Название функции, кол-во вызовов, дата-время последнего выполнения
# Пример:
# render, 10,  12.05.2022 12:00
# show,    5,  12.05.2022 12:02
# render, 15,  12.05.2022 12:07
#
# Декоратор должен применяться для различных функций с переменным числом аргументов.
# Статистику вызовов необходимо записывать в файл при каждом запуске скрипта.
import datetime

import time
from datetime import datetime

# Словарь для хранения статистики
function_stats = {}


def call_counter(func):
    def wrapper(*args, **kwargs):
        # Момент выполнения функции
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M")

        # Обновляем статистику
        if func.__name__ not in function_stats:
            function_stats[func.__name__] = {
                'count': 0,
                'last_time': current_time
            }

        function_stats[func.__name__]['count'] += 1
        function_stats[func.__name__]['last_time'] = current_time

        # Вызываем оригинальную функцию
        result = func(*args, **kwargs)

        # Записываем текущую статистику в файл
        with open('debug.log', 'a') as f:
            f.write(f"{func.__name__}, "
                    f"{function_stats[func.__name__]['count']}, "
                    f"{function_stats[func.__name__]['last_time']}\n")

        return result

    return wrapper


# Пример использования декоратора
@call_counter
def render():
    print("Выполняем")


@call_counter
def show():
    print("Показываем")

#Несколько вызовов функций
render()
show()
render()
render()
show()