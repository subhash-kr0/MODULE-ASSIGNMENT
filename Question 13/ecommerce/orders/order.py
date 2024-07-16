# orders/order.py

class Order:
    def __init__(self, order_number, products, total_amount):
        self.order_number = order_number
        self.products = products
        self.total_amount = total_amount

    def __str__(self):
        return f"Order Number: {self.order_number}, Total Amount: ${self.total_amount}"

def process_order(order):
    # Placeholder function to process an order
    print(f"Processing order: {order}")

# Additional order processing functions can be added as needed
