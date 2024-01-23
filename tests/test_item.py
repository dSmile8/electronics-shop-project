"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import *


def test_calculate_total_price(data):
    assert Item.calculate_total_price(data) == 125000.00


def test_apply_discount(data):
    Item.apply_discount(data)
    assert data.price == 12500.00
