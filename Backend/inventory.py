class Inventory:
    #dont have to do updating inventory
    def __init__(self, buns, wraps, patties, ingredients, sides, drinks):
        self.buns = buns
        self.wraps = wraps
        self.patties = patties
        self.ingredients = ingredients
        self.sides = sides
        self.drinks = drinks

    def add_bun(self, bun):
        self.buns.append(bun)

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

    def get_buns_amount(self):
        i = 1
        while True:
            try:
                for bun in self.buns:
                    print(str(i) + ".", bun.name, "has", str(bun.amount), "left")
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def decrease_bun(self, name, amount):
        for bun in self.buns:
            if bun.name == name:
                bun.amount -= amount

    def add_wrap(self, wrap):
        self.wraps.append(wrap)

    def get_wraps(self):
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

    def get_wraps_amount(self):
        i = 1
        while True:
            try:
                for wrap in self.wraps:
                    print(str(i) + ".", wrap.name, "has", str(wrap.amount), "left")
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def decrease_wrap(self, name, amount):
        for wrap in self.wraps:
            if wrap.name == name:
                wrap.amount -= amount

    def add_patty(self, patty):
        self.patties.append(patty)

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

    def get_patties_amount(self):
        i = 1
        while True:
            try:
                for patty in self.patties:
                    print(str(i) + ".", patty.name, "has", str(patty.amount), "left")
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def decrease_patty(self, name, amount):
        for patty in self.patties:
            if patty.name == name:
                patty.amount -= amount

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

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

    def get_ingredients_amount(self):
        i = 1
        while True:
            try:
                for ingredient in self.ingredients:
                    print(str(i) + ".", ingredient.name, "has", str(ingredient.amount), "left")
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def decrease_ingredient(self, name, amount):
        for ingredient in self.ingredients:
            if ingredient.name == name:
                ingredient.amount -= amount

    def add_side(self, side):
        self.sides.append(side)
    
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

    def get_sides_amount(self):
        i = 1
        while True:
            try:
                for side in self.sides:
                    print(str(i) + ".", side.name, "has", str(side.amount), "left")
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1

    def decrease_side(self, name, amount):
        for side in self.sides:
            if side.name == name:
                side.amount -= amount
    
    def add_drink(self, drink):
        self.drinks.append(drink)

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

    def get_drinks_amount(self):
        i = 1
        while True:
            try:
                for drink in self.drinks:
                    print(str(i) + ".", drink.name, "has", str(drink.amount), "left")
                    i += 1
                break
            except:
                print("Invalid input, please try again")
            i = 1
    
    def decrease_drink(self, name, amount):
        for drink in self.drinks:
            if drink.name == name:
                drink.amount -= amount

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
inventory.add_bun(brioche)
inventory.add_bun(sesame)
inventory.add_bun(sourdough)
# adding the wraps to the inventory
inventory.add_wrap(flatbread)

# adding the patties to the inventory
inventory.add_patty(beef)
inventory.add_patty(chicken)
inventory.add_patty(lamb)

# adding the ingredients to the inventory
inventory.add_ingredient(lettuce)
inventory.add_ingredient(tomato)
inventory.add_ingredient(cheese)
inventory.add_ingredient(onion)
inventory.add_ingredient(tomato_sauce)
inventory.add_ingredient(barbecue_sauce)

# adding the sides to the inventory
inventory.add_side(chips)
inventory.add_side(nuggets)
inventory.add_side(apple_pie)
inventory.add_side(soft_serve)

# adding the drinks to the inventory
inventory.add_drink(cola)
inventory.add_drink(fanta)
inventory.add_drink(sprite)