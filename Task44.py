#  1. Реализовать класса DB - синглтон. Экземляр класса(подключение) к PostgreSQL
#  должно быть единственным.

#  2. Реализовать  фабрику которая создает модели различных производителей


import psycopg2
from abc import ABC, abstractmethod
from datetime import datetime


# 1. Реализация Singleton для подключения к PostgreSQL
class DB:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DB, cls).__new__(cls)
            cls._instance.connection = psycopg2.connect(
                host="localhost",
                database="car_database",
                user="your_user",
                password="your_password"
            )
        return cls._instance

    def execute_query(self, query, params=None):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            self.connection.commit()
            return cursor.fetchall()


# 2. Абстрактный базовый класс для автомобилей
class AbstractCar(ABC):
    @abstractmethod
    def sold(self):
        pass

    @abstractmethod
    def discount(self):
        pass


# 3. Реализация класса Car с фабрикой
class Car(AbstractCar):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.creation_date = datetime.now()

    def __repr__(self):
        return f"Car(brand={self.brand}, model={self.model})"

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")

    @classmethod
    def make_lada(cls):
        return cls(brand="Lada", model="Granta")

    @classmethod
    def make_mercedes(cls):
        return cls(brand="Mercedes", model="E-Class")

    @classmethod
    def make_toyota(cls):
        return cls(brand="Toyota", model="Camry")


# Пример использования
if __name__ == "__main__":
    # Проверка Singleton
    db1 = DB()
    db2 = DB()
    print(db1 is db2)  # True

    # Использование фабрики
    car1 = Car.make_lada()
    car2 = Car.make_mercedes()
    car3 = Car.make_toyota()

    print(car1)
    print(car2)
    print(car3)

    car1.sold()
    car2.discount()