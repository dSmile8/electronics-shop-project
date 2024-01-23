import pytest
from src.item import *


@pytest.fixture
def data():
    return Item('Телефон', 12500.00, 10)