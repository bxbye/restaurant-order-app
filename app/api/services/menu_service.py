import os
import sys

sys.path.append(os.getcwd())
from app.api.models.menu import MenuItem

class MenuService:
    def __init__(self):
        self._menu_items = [] # all menu items is kept here.

    def add_menu_item(self, id, name, price, description):
        menu_item = MenuItem(id, name, price, description)
        self._menu_items.append(menu_item)
        return menu_item

    def get_menu_item_by_id(self, item_id):
        item_id = int(item_id)
        for menu_item in self._menu_items:
            if menu_item.id == item_id:
                return menu_item
        return None

    def get_menu_items(self):
        return self._menu_items

    def update_menu_item(self, item_id, name=None, price=None, description=None):
        menu_item = self.get_menu_item_by_id(item_id)
        if menu_item:
            if name is not None:
                menu_item.name = name
            if price is not None:
                menu_item.price = price
            if description is not None:
                menu_item.description = description
            return True
        return False

    def delete_menu_item(self, item_id):
        menu_item = self.get_menu_item_by_id(item_id)
        if menu_item:
            self._menu_items.remove(menu_item)
            return True
        return False

"""
# Create a MenuService instance
menu_service = MenuService()

# Add a menu item
menu_item1 = menu_service.add_menu_item(1, "Cheeseburger", 10.99, "A delicious cheeseburger")

# Get a menu item by ID
menu_item_by_id = menu_service.get_menu_item_by_id(1)

# Get all menu items
menu_items = menu_service.get_menu_items()

# Update a menu item
menu_service.update_menu_item(1, name="Double Cheeseburger", price=12.99)

# Delete a menu item
menu_service.delete_menu_item(1)

"""