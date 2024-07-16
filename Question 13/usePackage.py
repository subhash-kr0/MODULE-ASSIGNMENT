from ecommerce.products.product import Product, get_product_info
from ecommerce.orders.order import Order, process_order

# Create and use instances of Product and Order classes
product1 = Product("Laptop", 999.99, "High-performance laptop")
product2 = Product("Mouse", 19.99, "Wireless mouse")
print(get_product_info(product1))  # Output: Laptop: $999.99 - High-performance laptop

order1 = Order("ORD123", [product1, product2], 1019.98)
process_order(order1)  # Output: Processing order: Order Number: ORD123, Total Amount: $1019.98
