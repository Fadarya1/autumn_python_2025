# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # @property
    # def price(self):
    #     return self.price
    #
    # @price.setter
    # def price(self, price):
    #     if price <= 0:
    #         self.__price = 0
    #     else:
    #         self.__price = price

class Order:
    def __init__(self):
        self.products = []

    @property
    def total_price(self):
        return sum(product.price for product in self.products) #подсчет общей стоимости товаров из списка

    def add_product(self, product):
        self.products.append(product) #добавляет товар для подсчета общей суммы

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product) #удаляет товар из списка для подсчета общей стоимости

    # def add_product(self):
    #     self.total_price += self.products[name].price
    #
    # def remove_product(self):
    #     self.total_price -= Product(self.price)


    # def __getattr__(self, item, value):
    #     if item == 'add_product':
    #         self.total_price += self.Product.price
    # @property
    # def total_price(self):
    #     return self.total_price
    #
    # @total_price.setter
    # def total_price(self, total_price):
    #     def add_product(self):
    #         self.total_price += self.product.price
    #
    #     def remove_product(self):
    #         self.total_price -= self.product.price
# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12