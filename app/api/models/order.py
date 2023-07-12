# id, user_id, items, status, total_price
class Order:
    def __init__(self, id, user_id) -> None:
        self._id = id
        self._user_id = user_id
        self._items = []
        self._status = "Pending"
        self._total_price = 0.0
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
    def add_item(self, item):
        self._items.append(item)
        self._total_price += item.price
    # remove item from order item list
    def remove_item(self, item):
        self._items.remove(item)
        self._total_price -= item.price
