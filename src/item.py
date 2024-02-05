import csv
import os.path
from pathlib import Path


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
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]

        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_path):
        '''
        Инициализирует экземпляр класса Item данными из файла src/items.csv
        '''
        cls.all = []
        # file_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'items.csv')
        BASE_DIR = Path(__file__).resolve().parent.parent
        file = BASE_DIR / file_path
        with open(file, 'r', newline='', encoding="windows-1251") as csvfile:
            csvreader = csv.DictReader(csvfile)
            # header = next(csvreader)  # Пропускаем заголовок
            for row in csvreader:
                cls(str(row["name"]), float(row["price"]), int(row["quantity"]))


    @staticmethod
    def string_to_number(num_str):
        ''' Возвращает число '''
        float_num = float(num_str)
        int_num = int(float_num)
        if int_num != float_num:
            return float_num
        return int_num

    def __repr__(self):
        """
        ___repr___

        """
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        __str___

        """
        return self.__name
