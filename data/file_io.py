import json
import os
import sys
sys.path.append(os.getcwd())
from app.api.services import menu_service, user_service, order_service


class DataFile:
    def __init__(self, filename) -> None:
        self.filename = filename
    # read json file and fill user, menu, order services.
    def read_data(self):
        with open(self.filename, 'r') as file:
            data_dict = json.load(file)
        
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
        return s_user, s_menu, s_order
    # it's more complicated because # TypeError: Object of type MenuItem is not JSON serializable
    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
        
