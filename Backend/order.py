
class food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount


class Order:
    #operates in the same way as booking
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__ (self, sides, drinks):
        self._sides = sides
        self._drinks = drinks

    def totalCost(self):
        return self._sides.sidesprice() + self._drinks.drinkprices()

    def printTotal(self):
        print(self._sides.printSides())
        print(self._drinks.printDrinks())
