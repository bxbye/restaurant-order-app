class User:
    def __init__(self, id, name, email, password) -> None:
        self._id = id
        self._name = name
        self._email = email
        self._password = password
    def __str__(self) -> str:
        return f"id: {self._id}, name: {self._name}, email: {self._email}, password: {self._password}"
    # getters and setters
    @property
    def id(self):
        return self._id
    @property
    def name(self):
        return self._name
    @property
    def email(self):
        return self._email
    @name.setter
    def name(self, value):
        self._name = value
    @email.setter
    def email(self, value):
        self._email = value
    # I don't want to implement getter and setter for password attribute. Because user musn't learn it. Otherwise, I will create a method for update password.
    # methods
    def authenticate(self, email, password):
        if self._email == email and self._password == password:
            return True
        return False
    def update_password(self, password):
        # Optional: Check if the password is available for our security credentials.
        self._password = password