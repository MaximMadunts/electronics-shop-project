import csv


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

        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:11]
        else:
            self._name = value

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

    @staticmethod
    def instantiate_from_csv(fp):
        with open(fp, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            next(reader, None)
            for row in reader:
                Item.all.append(row)

    @staticmethod
    def string_to_number(s):
        return int(float(s))

