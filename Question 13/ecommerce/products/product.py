# products/product.py

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"{self.name} - ${self.price}"

def get_product_info(product):
    return f"{product.name}: ${product.price} - {product.description}"

# Additional product management functions can be added as needed
