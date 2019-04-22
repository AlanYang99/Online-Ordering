from main import *
from inventory import Food
import pickle

class Order:
    #operates in the same way as booking
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__ (self):
        self._mains = None
        self._sides = None
        self._drinks = None

    def set_mains(self,mains):
        self._mains = mains

    def set_sides(self,sides):
        self._sides = sides

    def set_drinks(self,drinks):
        self._drinks = drinks

    @property
    def total_cost(self):
        price = 0
        if(self._mains != None):
            price += self._mains.price
        if(self._sides != None):
            price += self._sides.price
        if(self._drinks != None):
            price += self._drinks.price
        return round(price,2)

    @property
    def print_total(self):
        output = ''
        if(self._mains != None):
            output += self._mains.display_mains
        if(self._drinks != None):
            output += self._drinks.get_drinks
        if(self._sides != None):
            output += self._sides.get_sides
        if(output == ''):
            return "No Orders Currently Made"
        return output
