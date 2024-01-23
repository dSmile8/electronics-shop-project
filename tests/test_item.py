"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_calculate_total_price(data):
    assert data.calculate_total_price() == 125000.00


def test_apply_discount(data):
    Item.pay_rate = 0.6
    data.apply_discount()
    assert data.price == 7500.00
