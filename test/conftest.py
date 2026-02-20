import pytest

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.product import Product
from src.category import Category

@pytest.fixture
def first_category():
    return Category(
        name="Смартфоны",
        description="Смартфоны средство коммуникации",
        products=[
            Product("Samsung Galaxy C23 Ultra","256GB, Серый цвет, 200MP камера",180000.0,5),
            Product("Galaxy C23", "256GB", 1800.0)
        ]
    )


@pytest.fixture
def second_category():
    return Category(
        name="TV",
        description="Телевизоры средство коммуникации",
        products=[
            Product("TV Galaxy C23 Ultra","200MP камера",100.0,1),
            Product("TV C23", "антена мощь, cnfhkbyr d gjlfhjr", 18.0)
        ]
    )


@pytest.fixture
def product1():
    return Product("Телефон", "Смартфон", 50000, 10)

@pytest.fixture
def product2():
    return Product("Книга", "Роман", 1000, 5)

@pytest.fixture
def product3():
    return Product("Ручка", "Шариковая", 50, 100)

@pytest.fixture
def sample_product():
    return Product("Test", "Desc", 100.0, "Cat", 5)

@pytest.fixture
def sample_category(sample_product):
    return Category("TestCat", "Desc", [sample_product])