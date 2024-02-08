from src.item import Item
from src.phone import Phone
import pytest


def test_repr():
    phone1 = Phone('Samsung22', 10000, 30, 2)
    assert repr(phone1) == "Phone('Samsung22', 10000, 30, 2)"


def test_number_of_sim():
    phone1 = Phone('Samsung22', 10000, 30, 2)
    assert phone1.number_of_sim == 2


def test_number_of_sim_setter():
    phone1 = Phone('Samsung22', 10000, 30, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(Exception):
        phone1.number_of_sim = 0

