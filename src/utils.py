import json
import os

from src.product import Product
from src.category import Category

def read_json(path: str) -> dict:
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    return data


def created_object_for_json(data):
    categories = []
    for category_data in data:
        products = []
        for product_item in category_data.get("products", []):
            products.append(Product(**product_item))
        category_data["products"] = products
        categories.append(Category(**category_data))
    return categories

if __name__ == "__main__":
    row_data = read_json('../data/products.json')
    users_data = created_object_for_json(row_data)
    print(users_data)