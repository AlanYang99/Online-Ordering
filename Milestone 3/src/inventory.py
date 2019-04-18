import pickle
class Food:
    '''
    Utility class for ingredients or food in general, which has the
    attributes: name, price, amount
    '''
    def __init__(self,name,price,amount):
        self._name = name
        self._price = price
        self._amount = amount

    def __str__(self):
        return f'{self._amount} x {self._name} : ${self._amount * self._price}\n'

    def __repr__(self):
        return f'{self._name},{self._price},{self._amount}'

class Inventory:

    @staticmethod
    def get_ingredients():
        infile = open("Ingredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_ingredients1():
        infile = open("Ingredients1",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory
    @staticmethod
    def get_burgerIngredients():
        infile = open("burgerIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_wrapIngredients():
        infile = open("wrapIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_sides():
        infile = open("sides",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_drinks():
        infile = open("drinks",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

print(inventory.get_ingredients())
print(inventory.get_burgerIngredients())
print(inventory.get_wrapIngredients())
print(inventory.get_sides())
print(inventory.get_drinks())
