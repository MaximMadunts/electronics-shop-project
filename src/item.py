import csv
import os.path
import pathlib
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
            Создание экземпляра класса item.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        """
        full_price = self.price * self.quantity
        return full_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        """
        Проверяет, что длина наименования товара не больше 10 симвовов.
        В противном случае,
        обрезать строку (оставить первые 10 символов)
        """
        if len(value) <= 10:
            self.__name = value

        else:
            self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, file_path):
        '''
        Инициализирует экземпляр класса Item данными из файла src/items.csv
        '''
        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), file_path)
        with open(file_path, 'r', newline='', encoding='windows-1251') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = cls.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num_str):
        ''' Возвращает число '''
        float_num = float(num_str)
        int_num = int(float_num)
        if float_num != int_num:
            return int_num
        return int_num

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Unsupported operand type. You can only add Item instances.")