class MenuItem:
    def __init__(self, id, name, price, description) -> None:
        self._id = id
        self._name = name
        self._price = price
        self._description = description
    def __str__(self) -> str:
        return f"id: {self._id}, name: {self._name}, price: {self._price}, description: {self.description}"
    # getters
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def price(self):
        return self._price
    @property
    def description(self):
        return self._description
    # setters
    @name.setter
    def name(self, value):
        # Optional: Add validation or additional logic here
        self._name = value
    @price.setter
    def price(self, value):
        # Optional: Add validation or additional logic here
        self._price = value
    @description.setter
    def description(self, value):
        # Optional: Add validation or additional logic here
        self._description = value
    