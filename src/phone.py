from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other):
        """
        Реализация возможности сложения экземпляров класса `Phone` и `Item`
        (сложение по количеству товара в магазине)
        """
        if isinstance(other, Item):
            return int(self.quantity) + int(other.quantity)
        elif isinstance(other, Phone):
            return int(self.quantity) + int(other.quantity)
