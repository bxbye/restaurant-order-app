import pytest
import os
import sys

sys.path.append(os.getcwd())
from app.api.services.order_service import OrderService, Order

def test_methods():
    assert 1 == 1
    
