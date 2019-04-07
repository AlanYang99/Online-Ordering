class Food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

class drinks:

    def __init__(self):
        self._can = [Food('coke',1.5,0),Food('fanta',1.5,0),Food('solo',1.5,0)]
        self._bottle = [Food('coke',2.5,0),Food('fanta',2.5,0),Food('solo',2.5,0)]

    def price(self):
        price = 0
        for i in self._can:
            price += i.amount * i.price
        for i in self._bottle:
            price += i.amount * i.price
        return price

    def set_cans(self,drink,amount):
        found = 0
        for i in self._can:
            if(i.name is drink):
                i.amount = amount
                found = 1
        if(found is 0):
            print('drink is not available')

    def set_bottles(self,drink,amount):
        found = 0
        for i in self._bottle:
            if(i.name is drink):
                i.amount = amount
                found = 1
        if(found is 0):
            print('drink is not available')

    def printDrinks(self):
        drinks = ''
        for i in self._can:
            drinks += f'{i.name} : {i.amount}\n'
        for i in self._bottle:
            drinks += f'{i.name} : {i.amount}\n'
        return drinks

drink1 = drinks()
drink1.set_cans('coke',2)
drink1.set_bottles('fanta',3)
"""
print(drink1.printDrinks())
print(drink1.price())
"""
