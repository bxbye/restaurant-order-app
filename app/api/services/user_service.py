import os
import sys

sys.path.append(os.getcwd())
from app.api.models.user import User

class UserService:
    def __init__(self):
        self._users = [] # all users are kept in here.

    def create_user(self, id, name, email, password):
        user = User(id, name, email, password)
        self._users.append(user)
        return user

    def get_user_by_id(self, user_id):
        for user in self._users:
            if user.id == user_id:
                return user
        return None

    def get_user_by_email(self, email):
        for user in self._users:
            if user.email == email:
                return user
        return None

    def update_user(self, user_id, name=None, email=None, password=None):
        user = self.get_user_by_id(user_id)
        if user:
            if name is not None:
                user.name = name
            if email is not None:
                user.email = email
            if password is not None:
                user.password = password
            return True
        return False

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            self._users.remove(user)
            return True
        return False

    def login(self, email, password):
        user = self.get_user_by_email(email)
        if user and user.authenticate(email, password):
            return user
        return None

"""
# Create a UserService instance
user_service = UserService()

# Create a new user
user = user_service.create_user(1, "John Doe", "johndoe@example.com", "password123")

# Get a user by ID
user_by_id = user_service.get_user_by_id(1)

# Get a user by email
user_by_email = user_service.get_user_by_email("johndoe@example.com")

# Update a user's information
user_service.update_user(1, name="Jane Doe")

# Delete a user
user_service.delete_user(1)

# Login with valid credentials
authenticated_user = user_service.login("johndoe@example.com", "password123")
if authenticated_user:
    print("Login successful!")
else:
    print("Invalid credentials.")
"""