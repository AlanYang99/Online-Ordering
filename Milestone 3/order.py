from main import *
from inventory import Food
import dill as pickle

class Order:
    #operates in the same way as booking
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__ (self, mains = None,sides = None, drinks = None):
        self._mains = mains
        self._sides = sides
        self._drinks = drinks


    @property
    def total_cost(self):
        price = 0
        price += self._mains.price
        price += self._sides.price
        price += self._drinks.price
        return price

    @property
    def print_total(self):
        output = ''
        if(self._mains != None):
            output += self._mains.displayMains
        if(self._drinks != None):
            output += self._drinks.get_drinks
        if(self._sides != None):
            output += self._sides.get_sides
        if(output == ''):
            return "No Orders Currently Made"
        return output