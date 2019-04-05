class food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

class drinks:

    def __init__(self,coke,fanta = None,solo = None):
        self.coke = coke
        self.fanta = fanta
        self.solo = solo

    def drinkprices(self):
        return self.coke.price * self.coke.amount #gonna finalise this later

    def printDrinks(self):
        return f'coke: {self.coke.amount}'
