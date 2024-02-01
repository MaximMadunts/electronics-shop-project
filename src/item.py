import csv
import os.path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
            Создание экземпляра класса item.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]

        else:
            self.__name = value


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        """

        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_path):
        '''
        Инициализирует экземпляр класса Item данными из файла src/items.csv
        '''
        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'items.csv')

        with open(file_path, 'r', newline='') as csvfile:
            csvreader = csv.DictReader(csvfile)
            # header = next(csvreader)  # Пропускаем заголовок
            for row in csvreader:
                # name, price, quantity = row
                # Item(name, price, quantity)
                cls(row['name'], row['price'], row['quantity'])


    @classmethod
    def print_all(cls):
        for row in cls.all:
            print(f"name: {row.name}, price: {row.price}, quantity: {row.quantity}")

    def string_to_number(s):
        return int(float(s))

