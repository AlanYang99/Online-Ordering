import pickle

class Food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

class drinks:

    def __init__(self):
        # self._can = [Food('coke',1.5,0),Food('fanta',1.5,0),Food('solo',1.5,0)]
        # self._bottle = [Food('coke',2.5,0),Food('fanta',2.5,0),Food('solo',2.5,0)]
        self._drinks = []

    def set_drinks(self, drink, amount):
        found = 0
        infile = open("drinks", "rb")
        drinks = pickle.load(infile)
        infile.close()
        for i in drinks:
            if(i.name is drink):
                self._drinks.append(Food(i._name, i._price, i._amount))
                found = 1
        if(found is 0):
            print("Ingredient is not found")

    def price(self):
        price = 0
        infile = open("drinks", "rb")
        drinks = pickle.load(infile)
        infile.close()
        for i in drinks:
            price += i._amount * i._price
        return price

    # def set_cans(self,drink,amount):
    #     found = 0
    #     for i in self._can:
    #         if(i.name is drink):
    #             i.amount = amount
    #             found = 1
    #     if(found is 0):
    #         print('drink is not available')

    # def set_bottles(self,drink,amount):
    #     found = 0
    #     for i in self._bottle:
    #         if(i.name is drink):
    #             i.amount = amount
    #             found = 1
    #     if(found is 0):
    #         print('drink is not available')

    def printDrinks(self):
        drinkList = ""
        infile = open("drinks", "rb")
        drinks = pickle.load(infile)
        infile.close()
        for i in drinks:
            drinkList += f'{i.name} : {i.amount}\n'
        return drinkList

# drink1 = drinks()
# drink1.set_cans('coke',2)
# drink1.set_bottles('fanta',3)
"""
print(drink1.printDrinks())
print(drink1.price())
"""
