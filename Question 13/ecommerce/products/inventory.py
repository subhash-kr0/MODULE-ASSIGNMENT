# products/inventory.py

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def list_products(self):
        return self.products

# Additional inventory management functions can be added as needed
