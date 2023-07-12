from fastapi import APIRouter
from app.api.services.menu_service import MenuService
router = APIRouter() # create router
menu = MenuService() # create menu service

"""
TODO:
1:
post operation of menu endpoint should get MenuItem object's parameter from client.
I could use faker library to create MenuItem object.
2:
all operations should return results with correct HTTP status code. for error: 404, for update: 201, for success: 200, etc.
"""

# get all menu items
@router.get("/menu")
def menu_of_restaurant():
    rest_menu = menu.get_menu_items()
    # format result data
    return rest_menu
# create a new item
@router.post("/menu")
def add_item_to_menu():
    total_item = len(menu.get_menu_items())
    new_item = menu.add_menu_item(id=total_item, name="Trilice", price=9.99, description="Uzerinde kahverengi gul yapraklari olan hafif br tatlidir.")
    return new_item

# get menu item by id
@router.get("/menu/{item_id}")
def get_item_by_id(item_id):
    item = menu.get_menu_item_by_id(item_id)
    if item:
        return item
    return {"message": "Item didn't find."}
# update menu item
@router.put("/menu/{item_id}")
def update_menu_item(item_id):
    result = menu.update_menu_item(item_id, name="Updated Name", description="Updated description.")
    if result:
        return menu.get_menu_item_by_id(item_id)
    return {"message": "Item couldn't update."}
# delete menu item
@router.delete("/menu/{item_id}")
def delete_menu_item(item_id):
    if menu.delete_menu_item(item_id):
        return {"message": f"Item {item_id} removed from menu."}
    return {"message": f"Item {item_id} couldn't remove from menu."}