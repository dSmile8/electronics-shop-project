"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone
import pytest


class Other:
    pass


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 125000.00


def test_apply_discount(data):
    Item.pay_rate = 0.6
    data.apply_discount()
    assert data.price == 7500.00


def test_instantiate_from_csv():
    assert isinstance(Item.instantiate_from_csv(), object)
    item1 = Item.instantiate_from_csv().all[3]
    assert item1.name == "Мышка"


def test_name():
    item1 = Item('Наушники', 1500, 20)
    assert item1.name == 'Наушники'
    with pytest.raises(Exception):
        item1.name = 'БольшиеНаушники'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Phone('iPhone12', 50000, 12, 1)
    item3 = Other()

    assert item1 + item2 == 32
    assert item1 + item3 is None
