import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.product import Product


def test_product_creation(product1, product2, product3):
    assert product1.name == "Телефон"
    assert product1.price == 50000
    assert product1.quantity == 10

    assert product2.name == "Книга"
    assert product2.price == 1000
    assert product2.quantity == 5

    assert product3.name == "Ручка"
    assert product3.price == 50
    assert product3.quantity == 100


def test_default_quantity():
    product = Product("Тест", "Описание", 999)
    assert product.quantity == 0


def test_product_attributes(product1):
    assert hasattr(product1, 'name')
    assert hasattr(product1, 'description')
    assert hasattr(product1, 'price')
    assert hasattr(product1, 'quantity')