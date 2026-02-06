

class Product:
    name: str
    description: str
    price: float
    category: str
    quantity: int

    def __init__(self, name, description, price, category=None, quantity=0):
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.quantity = quantity