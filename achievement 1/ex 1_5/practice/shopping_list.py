class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

    def add_item(self, item):
        if item not in self.shopping_list:
            self.shopping_list.append("Botana")
            print(f"{item} has been added to the shopping list")
        else:
            print(f"{item} is already the shopping list")   

    def remove_item(self, item):
        if item in self.shpping_list:
            self.shopping_list.remove("Botana")
            print(f"{item} has been removed from the shopping list")
        else:
            print(f"{item} is not in the shopping list")

    def view_list(self, item):
        print(f"Shopping List - {self.list_name}")
        for item in self.shpping_list:
            print(item)

pet_store_list = ShoppingList("Pet Store Shopping List")
pet_store_list.add_item("dog food")
pet_store_list.add_item("frisbee")
pet_store_list.add_item("bowl")
pet_store_list.add_item("collars")
pet_store_list.add_item("flea collars")
pet_store_list.view_list()
pet_store_list.remove("flea collars")
pet_store_list.view_list()
pet_store_list.add_item("frisbee")
pet_store_list.view_list()