class MenuItem:
    _id_counter = 1  # Class-level attribute to generate unique IDs
    
    def __init__(self, name, description, price, category):
        self._id = MenuItem._id_counter  # Unique ID
        MenuItem._id_counter += 1
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def get_id(self):
        return self._id

    def update_info(self, name=None, description=None, price=None, category=None):
        if name:
            self.name = name
        if description:
            self.description = description
        if price:
            self.price = price
        if category:
            self.category = category

    def __str__(self):
        return f"{self.name} ({self.category}): {self.description} - ${self.price:.2f}"


class FoodItem(MenuItem):
    def __init__(self, name, description, price, is_vegan=False, is_gluten_free=False):
        super().__init__(name, description, price, category="Food")
        self.is_vegan = is_vegan
        self.is_gluten_free = is_gluten_free

    def __str__(self):
        vegan_str = " (Vegan)" if self.is_vegan else ""
        gluten_free_str = " (Gluten-Free)" if self.is_gluten_free else ""
        return super().__str__() + vegan_str + gluten_free_str


class BeverageItem(MenuItem):
    def __init__(self, name, description, price, is_alcoholic=False):
        super().__init__(name, description, price, category="Beverage")
        self.is_alcoholic = is_alcoholic

    def __str__(self):
        alcoholic_str = " (Alcoholic)" if self.is_alcoholic else ""
        return super().__str__() + alcoholic_str


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item}")

    def update_item(self, item_id, name=None, description=None, price=None, category=None):
        for item in self.items:
            if item.get_id() == item_id:
                item.update_info(name, description, price, category)
                print(f"Updated: {item}")
                return
        print("Item not found.")

    def remove_item(self, item_id):
        for item in self.items:
            if item.get_id() == item_id:
                self.items.remove(item)
                print(f"Removed: {item}")
                return
        print("Item not found.")

    def display_menu(self):
        print("Menu:")
        for item in self.items:
            print(item)


# Testing the Restaurant Management System

# Create the menu
menu = Menu()

# Add food items
food1 = FoodItem(name="Burger", description="Beef patty with lettuce and tomato", price=8.99, is_gluten_free=False)
food2 = FoodItem(name="Salad", description="Fresh greens with vinaigrette", price=5.99, is_vegan=True)
menu.add_item(food1)
menu.add_item(food2)

# Add beverage items
beverage1 = BeverageItem(name="Coffee", description="Hot brewed coffee", price=2.99, is_alcoholic=False)
beverage2 = BeverageItem(name="Wine", description="Red wine glass", price=6.99, is_alcoholic=True)
menu.add_item(beverage1)
menu.add_item(beverage2)

# Display menu
menu.display_menu()

# Update a menu item
menu.update_item(food1.get_id(), price=9.49)

# Remove a menu item
menu.remove_item(beverage2.get_id())

# Display menu after updates
menu.display_menu()
