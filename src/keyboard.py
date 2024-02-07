from src.item import Item


class LanguageMixin:
    LanguageMixin = {'EN', 'RU'}

    def __init__(self):
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Меняет атрибут клавиатуры language (раскладку клавиатуры).
        """
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'


class Keyboard(Item, LanguageMixin):
    @property
    def language(self):
        return self._language

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        LanguageMixin.__init__(self)
    #     self._language = 'EN'
    #
    # @property
    # def language(self):
    #     return self._language
    #
    # def __repr__(self):
    #     return f"Keyboard('{self.name}', {self.price}, {self.quantity})"
    #
    # def change_lang(self):
    #     if self._language == 'EN':
    #         self._language = 'RU'
    #     else:
    #         self._language = 'EN'
    @language.setter
    def language(self, value):
        self._language = value
