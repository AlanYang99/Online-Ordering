class Inventory:
    #dont have to do updating inventory
    def __init__(self, buns, wraps, patties, ingredients, sides, drinks):
        #self._inventory = {}
        self.buns = buns
        self.wraps = wraps
        self.patties = patties
        self.ingredients = ingredients
        self.sides = sides
        self.drinks = drinks

    def get_buns(self):
        i = 1
        while True:
            try:
                for bun in self.buns:
                    print(str(i) + ".", bun.name)
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def get_warps(self):
        i = 1
        while True:
            try:
                for wrap in self.wraps:
                    print(str(i) + ".", wrap.name)
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def get_patties(self):
        i = 1
        while True:
            try:
                for patty in self.patties:
                    print(str(i) + ".", patty.name)
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def get_ingredients(self):
        i = 1
        while True:
            try:
                for ingredient in self.ingredients:
                    print(str(i) + ".", ingredient.name)
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1
    
    def get_sides(self):
        i = 1
        while True:
            try:
                for side in self.sides:
                    print(str(i) + ".", side.name)
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def get_drinks(self):
        i = 1
        while True:
            try:
                for drink in self.drinks:
                    print(str(i) + ".", drink.name)
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

class Food:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

# turning inventory into an object
inventory = Inventory([], [], [], [], [], [])

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
inventory.buns.append(brioche)
inventory.buns.append(sesame)
inventory.buns.append(sourdough)

# adding the wraps to the inventory
inventory.wraps.append(flatbread)

# adding the patties to the inventory
inventory.patties.append(beef)
inventory.patties.append(chicken)
inventory.patties.append(lamb)

# adding the ingredients to the inventory
inventory.ingredients.append(lettuce)
inventory.ingredients.append(tomato)
inventory.ingredients.append(cheese)
inventory.ingredients.append(onion)
inventory.ingredients.append(tomato_sauce)
inventory.ingredients.append(barbecue_sauce)

# adding the sides to the inventory
inventory.sides.append(chips)
inventory.sides.append(nuggets)
inventory.sides.append(apple_pie)
inventory.sides.append(soft_serve)

# adding the drinks to the inventory
inventory.drinks.append(cola)
inventory.drinks.append(fanta)
inventory.drinks.append(sprite)

inventory.get_buns()
print("")
inventory.get_warps()
print("")
inventory.get_patties()
print("")
inventory.get_ingredients()
print("")
inventory.get_sides()
print("")
inventory.get_drinks()