from src.product import Product

def test_product_creation(product):
    assert product.name == "iPhone 15"
    assert product.description == "Смартфон Apple"
    assert product.price == 999.99
    assert product.category == "Смартфоны"
    assert product.quantity == 10

def test_product_default_values():
    product = Product("Xiaomi", "Android phone", 500.0)
    assert product.category is None
    assert product.quantity == 0