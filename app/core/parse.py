"""
db olarak kullanilan data.json dosyasindaki users, menu, orders verilerini okuyup parse edip icindeki verilerden User, Order, MenuItem objeleri olustur. 
Servislerin listelerini gunceller. Program bu verileri kullanarak devam eder.
"""
import json
import os
import sys

sys.path.append(os.getcwd())
from data.file_io import DataFile
from app.api.services import menu_service, user_service, order_service
from app.api.models import menu, user, order
db_data_file = "data/data.json"
data_file = DataFile(db_data_file)
data_dict = data_file.read_data()
#print(data_dict)
s_user = user_service.UserService()
s_menu = menu_service.MenuService()
s_order = order_service.OrderService()

# get users data from file
users = data_dict["users"]
for item in users:
    #print(f"id: {user['id']}, name: {user['name']}, email: {user['email']}, password: {user['password']}")
    s_user.create_user(item["id"], item["name"], item["email"], item["password"])
# get menu data from file
menu_list = data_dict["menu"]
for item in menu_list:
    #print(f"id: {item['id']}, name: {item['name']}, price: {item['price']}, description: {item['description']}")
    s_menu.add_menu_item(item['id'], item['name'], item['price'], item['description'])
# get orders data from file
orders = data_dict["orders"]
for order in orders:
    # parse items of order and add to order list
    menu_items = order["items"]
    order_items = []
    for item in menu_items:
        new_item = s_menu.get_menu_item_by_id(item)
        order_items.append(new_item)
    s_order.create_order(id=order["id"], user_id=order["user_id"], items=order_items)

"""
for item in s_menu.get_menu_items():
    print(item)
for item in s_order.get_orders():
    print(item)
for item in s_user.get_users():
    print(item)
"""

"""
# Create object instances
person1 = Person("John Doe", 30)
person2 = Person("Jane Smith", 25)
person3 = Person("Bob Johnson", 40)

# Create object array
persons = [person1, person2, person3]

# Serialize objects to JSON array
json_data = json.dumps([vars(person) for person in persons])

# Print the JSON array
print(json_data)
"""
# decoding for write to data.json file


users = s_user.get_users()
json_data = json.dumps([vars(user) for user in users])
print(json_data)

my_menu = s_menu.get_menu_items()
json_data = json.dumps([vars(item) for item in my_menu])
print(json_data)

# TypeError: Object of type MenuItem is not JSON serializable
""" my_orders = s_order.get_orders()
json_data = json.dumps([vars(item) for item in my_orders])
print(json_data)
 """
