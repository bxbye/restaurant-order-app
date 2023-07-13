import pytest
import os
import sys

sys.path.append(os.getcwd())
from app.api.services.user_service import UserService, User

def test_methods():
    assert 1 == 1
    