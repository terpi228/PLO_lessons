

def test_category(first_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == "Смартфоны средство коммуникации"

    assert len(first_category.products) == 2
    assert first_category.products[0].name == "Samsung Galaxy C23 Ultra"
    assert first_category.products[1].name == "Galaxy C23"
    print("✅")


def test_second_category(second_category):
    assert second_category.name == "TV"
    assert second_category.description == "Телевизоры средство коммуникации"

    assert len(second_category.products) == 2
    assert second_category.products[0].name == "TV Galaxy C23 Ultra"
    assert second_category.products[1].name == "TV C23"
    assert second_category.products[0].price == 100.0
    assert second_category.products[1].price == 18.0
    print("✅")