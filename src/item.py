import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []
    DATA_DIR = Path(__file__).parent.joinpath('items.csv')

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
        self.all.append(self)  # идём к списку и добавляем self, то есть сам экземпляр

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return other.quantity + self.quantity
        else:
            return None


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv_"""

        with cls.DATA_DIR.open(newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            cls.all.clear()
            for row in reader:
                print(row['name'], row['price'], row['quantity'])
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, price, quantity)
            return cls

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):

        if len(new_name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов")
        else:
            self.__name = new_name
