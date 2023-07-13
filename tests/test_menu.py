import pytest
import os
import sys

sys.path.append(os.getcwd())
from app.api.models.menu import MenuItem

# writing tests for MenuItem class
def test_menu_item_attributes():
    menu_item = MenuItem(1, "Cheeseburger", 10.99, "A delicious cheeseburger")
    
    assert menu_item.id == 1
    assert menu_item.name == "Cheeseburger"
    assert menu_item.price == 10.99
    assert menu_item.description == "A delicious cheeseburger"
