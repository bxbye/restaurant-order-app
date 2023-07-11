import pytest
import os
import sys
sys.path.append(os.getcwd())
from app.api.models.menu import MenuItem
from app.api.models.order import Order

def test_order_attributes():
    item1 = MenuItem(1, "Cheeseburger", 10.99, "A delicious cheeseburger")
    item2 = MenuItem(2, "French Fries", 4.99, "Crispy and golden fries")
    
    order = Order(1, 123)
    order.add_item(item1)
    order.add_item(item2)
    
    assert order.id == 1
    assert order.user_id == 123
    assert len(order.items) == 2
    assert order.status == "Pending"

def test_order_total_price():
    item1 = MenuItem(1, "Cheeseburger", 10.99, "A delicious cheeseburger")
    item2 = MenuItem(2, "French Fries", 4.99, "Crispy and golden fries")
    
    order = Order(1, 123)
    order.add_item(item1)
    order.add_item(item2)
    
    total_price = order.total_price
    assert total_price == 15.98
