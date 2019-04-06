from inventory import *

class System:
    def __init__(self):
        self._order_list = {} #id:order
        self._staff = {} #username"password

    def start_order(self):
        choice = input("Beginning order:\nWould you like to order a main?\n1. Yes\n2. No\n")
        if choice == "1":
            choice = input("What would you like?\n1. Burger\n2.Wrap?\n")
            if choice == "1":
                print("Choose what you want.")
                inventory.get_buns()

    # def delete_order(self, order_id):
    #     if order_id in self._order_list:
    #         #remove

system = System()

# # checking functions and testing
# inventory.get_buns()
# print("")
# inventory.get_wraps()
# print("")
# inventory.get_patties()
# print("")
# inventory.get_ingredients()
# print("")
# inventory.get_sides()
# print("")
# inventory.get_drinks()
# print("")
# inventory.get_buns_amount()
# print("")
# inventory.get_wraps_amount()
# print("")
# inventory.get_patties_amount()
# print("")
# inventory.get_ingredients_amount()
# print("")
# inventory.get_sides_amount()
# print("")
# inventory.get_drinks_amount()
# print("")
# inventory.decrease_bun("Brioche Bun", 1)
# print("")
# inventory.get_buns_amount()
# print("")
# inventory.decrease_bun("Sesame Seed Bun", 2)
# print("")
# inventory.get_buns_amount()
# print("")
# inventory.decrease_wrap("Flatbread", 3)
# print("")
# inventory.get_wraps_amount()
# print("")
# inventory.decrease_patty("Beef Patty", 4)
# print("")
# inventory.get_patties_amount()
# print("")
# inventory.decrease_ingredient("Cheese", 5)
# print("")
# inventory.get_ingredients_amount()
# print("")
# inventory.decrease_side("Nugget", 6)
# print("")
# inventory.get_sides_amount()
# print("")
# inventory.decrease_drink("Cola", 7)
# print("")
# inventory.get_drinks_amount()

system.start_order()