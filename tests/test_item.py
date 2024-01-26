"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


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