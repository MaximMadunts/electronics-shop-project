import csv
import os
from typing import Type


class InstantiateCSVError(Exception):
    def __init__(self, *args, **kwargs):
        self.massage = "Файл item.csv поврежден"


class FileNotFoundError(Exception):
    def __init__(self, *args, **kwargs):
        self.massage = "Отсутствует файл item.csv"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        cost_product = self.price * self.quantity
        return cost_product

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
            print(f'Корректное название - {value}')
        else:
            self.__name = value[:10]
            print(f'Длинное слово - {value[:10]}')

    @classmethod
    def instantiate_from_csv(cls):
        '''
        Инициализирует экземпляр класса Item данными из файла src/items.csv
        '''

        cls.all.clear()
        file_path = os.path.join(os.path.dirname(__file__), 'items.csv')
        try:
            with open(file_path, 'r', newline='', encoding='windows-1251') as csvfile:
                csvreader = csv.DictReader(csvfile)
                for row in csvreader:
                    cls(str(row['name']), float(row['price']), int(row['quantity']))

        except FileNotFoundError:
            raise FileNotFoundError
        except KeyError:
            raise InstantiateCSVError


    @staticmethod
    def string_to_number(name):
        """
        Статический метод, возвращающий число из числа-строки
        """
        return int(float(name))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.name}'

    def __add__(self, other):
        """
        Реализация возможности сложения экземпляров класса `Phone` и `Item`
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return self.quantity + other.quantity
        return ValueError("Складывать можно только объекты классов с родительским классом Item")
