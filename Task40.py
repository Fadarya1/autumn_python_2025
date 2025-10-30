# Система уведомлений (Полиморфизм)
# todo: Реализовать систему отправки уведомлений пользователям через разные каналы.
#
# Требования:
# Базовый класс NotificationSender с методом send(message, user)


class NotificationSender:
    def send(self, user, message):
        self.message = message
        self.user = user

# EmailSender: отправляет email с темой "Образовательная платформа"
class EmailSender(NotificationSender):
    def send(self, user, message):
        print(f"Email for {user.name}:\nТема: 'Образовательная платформа'\n {message}")

# SMSSender: отправляет SMS (первые 50 символов сообщения)
class SMSSender(NotificationSender):
    def send(self, user, message):
        print(f"SMS for {user.name}:\n{message[:50]}")

# PushSender: отправляет push-уведомление с иконкой "🎓"
class PushSender(NotificationSender):
    def send(self, message, user):
        self.message = None
        self.user = user
        print("🎓")


class User:
    def __init__(self, name, preferred_notifications):
        self.name = name
        self.preferred_notifications = preferred_notifications

def notify_user(self, message):
    for item in self.preferred_notifications:
        item.send(self, message)

# Дочерние классы:


#
# Класс пользователя User:
# Свойства: name, preferred_notifications (список объектов NotificationSender)


# Этот код должен работать после реализации:
user = User("Мария", [EmailSender(), PushSender()])
notify_user(user, "Блок аналитики начинается с 27 октября!")

def notify_user(user, message):
    for sender in user.preferred_notifications:
        sender.send(message, user)