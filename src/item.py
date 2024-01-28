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

    def instantiate_from_csv(file_path):
        with open(file_path, 'r') as csvfile:
            csvreader = csv.DictReader(csvfile)
            # header = next(csvreader)  # Пропускаем заголовок
            for row in csvreader:
                # name, price, quantity = row
                # Item(name, price, quantity)
                Item(row['name'], row['price'], row['quantity'])
                print(row)

    @classmethod
    def print_all(cls):
        for row in cls.all:
            print(f"name: {row.name}, price: {row.price}, quantity: {row.quantity}")

    def string_to_number(s):
        return int(float(s))
