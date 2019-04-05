class Inventory:
    #dont have to do updating inventory
    def __init__(self, buns, wraps, patties, ingredient, sides, drinks):
        #self._inventory = {}
        self.buns = buns
        self.wraps = {}
        self.patties = {}
        self.ingredient = {}
        self.sides = {}
        self.drinks = {}

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

class Bun:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

brioche = Bun("Brioche Bun", 1, 100)
sesame = Bun("Sesame Seed Bun", 1, 100)
sourdough = Bun("Sourdough Bun", 1, 100)

inventory = Inventory([], [], [], [], [], [])

inventory.buns.append(brioche)
inventory.buns.append(sesame)
inventory.buns.append(sourdough)

inventory.get_buns()