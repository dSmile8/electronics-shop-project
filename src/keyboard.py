from src.item import Item


class MixinSavelanguage:
    def __init__(self):
        self._language = None

    def default_lang(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'
        return self


class Keyboard(Item, MixinSavelanguage):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinSavelanguage.default_lang(self)

    @property
    def language(self):
        return self._language
