class Inventory:
    #dont have to do updating inventory
    def __init__(self):
        self.inventory = []
        self.buns = []
        self.wraps = []
        self.patties = []
        self.ingredients = []
        self.sides = []
        self.drinks = []

    def add_bun(self, name, price, amount):
        self.buns.append((name, price, amount))

    def get_buns(self):
        i = 1
        for bun in self.buns:
            print(str(i) + ".", bun)
            i += 1
        i = 1

    def decrease_bun(self, name):
        for bun in self.buns:
            if bun.name == name:
                bun.amount -= 1

    def add_wrap(self, name, price, amount):
        self.wraps.append((name, price, amount))

    def get_wraps(self):
        i = 1
        for wrap in self.wraps:
            print(str(i) + ".", wrap)
            i += 1
        i = 1

    def decrease_wrap(self, name):
        for wrap in self.wraps:
            if wrap.name == name:
                wrap.amount -= 1

    def add_patty(self, name, price, amount):
        self.patties.append((name, price, amount))

    def get_patty(self):
        i = 1
        for patty in self.patties:
            print(str(i) + ".", patty)
            i += 1
        i = 1

    def decrease_patty(self, name):
        for patty in self.patties:
            if patty.name == name:
                patty.amount -= 1

class Food:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

# turning inventory into an object
#inventory = Inventory([], [], [], [], [], [])

# how adding the food works
# <generic name for the item> = Food(<"name">, <price>, <amount>)

# creating a list of buns
brioche = Food("Brioche Bun", 1, 100)
sesame = Food("Sesame Seed Bun", 1, 100)
sourdough = Food("Sourdough Bun", 1, 100)

# creating a list of wraps
flatbread = Food("Flatbread", 1, 100)

# creating a list of patties
beef = Food("Beef Patty", 1, 100)
chicken = Food("Chicken Patty", 1, 100)
lamb = Food("Lamb Patty", 1, 100)

# creating a list of ingredients
lettuce = Food("Lettuce", 1, 100)
tomato = Food("Tomato", 1, 100)
cheese = Food("Cheese", 1, 100)
onion = Food("Onion", 1, 100)
tomato_sauce = Food("Tomato Sauce", 1, 100)
barbecue_sauce = Food("Barbecue Sauce", 1, 100)

# creating a list of sides
chips = Food("Chip", 1, 100)
nuggets = Food("Nugget", 1, 100)
apple_pie = Food("Apple pie", 1, 100)
soft_serve = Food("Soft Serve", 1, 100)

# creating a list of drinks
cola = Food("Cola", 1, 100)
fanta = Food("Fanta", 1, 100)
sprite = Food("Sprite", 1, 100)

# adding the buns to the inventory
inventory = Inventory()

inventory.add_bun("Brioche Bun", 1, 100)
# Inventory.buns.append(brioche)
# Inventory.buns.append(sesame)
# Inventory.buns.append(sourdough)

# # adding the wraps to the inventory
# inventory.wraps.append(flatbread)

# # adding the patties to the inventory
# inventory.patties.append(beef)
# inventory.patties.append(chicken)
# inventory.patties.append(lamb)

# # adding the ingredients to the inventory
# inventory.ingredients.append(lettuce)
# inventory.ingredients.append(tomato)
# inventory.ingredients.append(cheese)
# inventory.ingredients.append(onion)
# inventory.ingredients.append(tomato_sauce)
# inventory.ingredients.append(barbecue_sauce)

# # adding the sides to the inventory
# inventory.sides.append(chips)
# inventory.sides.append(nuggets)
# inventory.sides.append(apple_pie)
# inventory.sides.append(soft_serve)

# # adding the drinks to the inventory
# inventory.drinks.append(cola)
# inventory.drinks.append(fanta)
# inventory.drinks.append(sprite)

# checking functions and testing

inventory.get_buns()
print("")
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
inventory.decrease_bun("Brioche Bun")
print("")
inventory.get_buns_amount()
print("")
# inventory.decrease_bun("Sesame Seed Bun")
# print("")
# inventory.get_buns_amount()
# print("")
# inventory.decrease_wrap("Flatbread")
# print("")
# inventory.get_wraps_amount()
# print("")
# inventory.decrease_patty("Beef Patty")
# print("")
# inventory.get_patties_amount()
# print("")
# inventory.decrease_ingredient("Cheese")
# print("")
# inventory.get_ingredients_amount()
# print("")
# inventory.decrease_side("Nugget")
# print("")
# inventory.get_sides_amount()
# print("")
# inventory.decrease_drink("Cola")
# print("")
# inventory.get_drinks_amount()