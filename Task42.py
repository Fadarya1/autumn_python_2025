class ErrorWrongNumber(ValueError):
    def __init__(self):
        self.code = 1000
        self.message = "Значение должно быть в диапазоне от 5 до 10"

number = int(input("Введите число: "))
if number not in range (5, 10):
    raise ErrorWrongNumber()

class EmptyStringError(ValueError):
    def __init__(self):
        self.code = 1001
        self.message = "Вернулась пустая строка"

letter = input()
if letter is None:
    raise EmptyStringError()

class ConnectionAttemptError(ConnectionError):
    def __init__(self, message="Произошел разрыв соединения с сервером"):
        self.code = 1002
        self.message = message
        super().__init__(self.message)

def connect_to_server():
    try:
        # Имитация попытки подключения к серверу
    except  ConnectionAttemptError as e:
        print(f"Обработано исключение: {e}")
    #______________________________________________________________
