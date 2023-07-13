import pytest
import os
import sys

sys.path.append(os.getcwd())
from app.api.services.menu_service import MenuService, MenuItem

def test_menu_service_methods():
    menu = MenuService()

    menu.add_menu_item(1, "Cheeseburger", 10.99, "A delicious cheeseburger")
    assert len(menu.get_menu_items()) == 1

    new_item = MenuItem(1, "Cheeseburger", 10.99, "A delicious cheeseburger")
    item = menu.get_menu_item_by_id(1)
    assert item.id == new_item.id
    assert item.name == new_item.name
    assert item.price == new_item.price
    assert item.description == new_item.description

    assert menu.update_menu_item(item_id=1, name="New Cheeseburger", price=15.00, description="New Cheeseburger") == True
    assert menu.update_menu_item(item_id=10, name="New Cheeseburger") == False
    
    assert menu.delete_menu_item(item_id=1) == True
    assert menu.delete_menu_item(item_id=1) == False
    