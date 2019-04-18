from main import *
from inventory import Food
import pickle

class Order:
    #operates in the same way as booking
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__ (self, mains = None,sides = None, drinks = None):
        self._mains = mains
        self._sides = sides
        self._drinks = drinks

    @property
    def totalCost(self):
        price = 0
        price += self._mains.price
        price += self._sides.price
        price += self._drinks.price
        return price

    @property
    def printTotal(self):
        output = ''
        output += self._mains.displayMains
        output += self._drinks.get_drinks
        output += self._sides.get_sides
        return output
