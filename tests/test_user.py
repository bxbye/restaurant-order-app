import pytest
import os
import sys

sys.path.append(os.getcwd())
from app.api.models.user import User


def test_user_attributes():
    user = User(1, "John Doe", "johndoe@example.com", "password123")
    
    assert user.id == 1
    assert user.name == "John Doe"
    assert user.email == "johndoe@example.com"

def test_user_authentication():
    user = User(1, "John Doe", "johndoe@example.com", "password123")
    
    assert user.authenticate("johndoe@example.com", "password123") == True
    assert user.authenticate("johndoe@example.com", "wrongpassword") == False
    assert user.authenticate("wrongemail@example.com", "password123") == False
