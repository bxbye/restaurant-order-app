import os
import sys

sys.path.append(os.getcwd())
from app.api.models.order import Order

class OrderService:
    def __init__(self):
        self._orders = [] # all orders are kept in here.

    def create_order(self, id, user_id, items=None, status=None):
        order = Order(id, user_id, items, status)
        self._orders.append(order)
        return order

    def get_order_by_id(self, order_id):
        for order in self._orders:
            if order.id == order_id:
                return order
        return None

    def get_orders_by_user_id(self, user_id):
        user_orders = []
        for order in self._orders:
            if order.user_id == user_id:
                user_orders.append(order)
        return user_orders

    def get_orders(self):
        return self._orders

    def update_order_status(self, order_id, status):
        order = self.get_order_by_id(order_id)
        if order:
            order.status = status
            return True
        return False

    def delete_order(self, order_id):
        order = self.get_order_by_id(order_id)
        if order:
            self._orders.remove(order)
            return True
        return False
"""
# Create an OrderService instance
order_service = OrderService()

# Create a new order
order = order_service.create_order(1, 123)  # Order ID: 1, User ID: 123

# Get an order by ID
order_by_id = order_service.get_order_by_id(1)

# Get orders by user ID
user_orders = order_service.get_orders_by_user_id(123)

# Update an order's status
order_service.update_order_status(1, "Delivered")

# Delete an order
order_service.delete_order(1)

"""