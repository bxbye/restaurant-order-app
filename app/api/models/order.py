# id, user_id, items, status, total_price
from app.api.models.menu import MenuItem

class Order:
    # constuctor can be invoked with items or without items.
    def __init__(self, id, user_id, items, status) -> None:
        self._id = id
        self._user_id = user_id
        self._items = items or []
        if status:
            self._status = status
        else:
            self._status = "Pending"
        self._total_price = 0.0
        if items:
            for item in self._items:
                self._total_price += item.price
    
    def __str__(self) -> str:
        order_items = ', '.join([str(item.id) for item in self._items])
        return f"id: {self._id}, user_id: {self.user_id}, order_items: [{order_items}], status: {self._status}, total_price: {self._total_price}"
    # getters
    @property
    def id(self):
        return self._id
    @property
    def user_id(self):
        return self._user_id
    @property
    def items(self):
        return self._items
    @property
    def status(self):
        return self._status
    @property
    def total_price(self):
        return self._total_price
    #setters
    @status.setter
    def status(self, value):
        self._status = value
    #methods
    # adds item to order items list
    def add_item(self, item: MenuItem):
        self._items.append(item)
        self._total_price += item.price
    # remove item from order item list
    def remove_item(self, item: MenuItem):
        self._items.remove(item)
        self._total_price -= item.price
