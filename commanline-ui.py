from data.file_io import DataFile

json_file = DataFile("data/data.json")
users, menu, orders = json_file.read_data()
print('Users...')
for item in users.get_users():
    print(item)
print('Menu...')
for item in menu.get_menu_items():
    print(item)
print('Orders...')
for item in orders.get_orders():
    print(item)

"""
All methods and services can run from this file.
"""
# add user
users.create_user(len(users.get_users())+1, 'Kadir KAYA', 'kdrky57@gmail.com', 'password123')
