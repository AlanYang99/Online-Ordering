#import pickle
import dill as pickle

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
        infile = open("src/Ingredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_ingredients1():
        infile = open("src/Ingredients1",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_burgerIngredients():
        infile = open("src/burgerIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_wrapIngredients():
        infile = open("src/wrapIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def get_sides():
        infile = open('src/sides','rb') 
        sides = pickle.load(infile)
        infile.close()
        return sides

    @staticmethod
    def get_drinks():
        infile = open("src/drinks",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

#inventory=Inventory()
#print(inventory.get_ingredients())
#print(inventory.get_burgerIngredients())
#print(inventory.get_wrapIngredients())
#print(inventory.get_sides())
#print(inventory.get_drinks())
