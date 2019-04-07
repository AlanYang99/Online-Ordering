from mains2 import *
from inventory1 import Food
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

# Ing = Ingredients()
# Ing.set_ingredients('bacon',4)
# burg1 = burgerIngredients()
# burg1.set_burgerIngredients('brioche bun',1)
# b = burgers(Ing,burg1)
# wrap1 = wrapIngredients()
# wrap1.set_wrapIngredients('flatbread',1)
# w = wraps(Ing,wrap1)
# meal1 = meals()
# meal1.addBurger(b)
# meal1.addWrap(w)
#
#
#
#
# side1 = sides()
# side1.set_sides('chips',10)
# drink1 = drinks()
# drink1.set_drinks('cola',10)
#
# ord = Order(meal1,side1,drink1)
# print(ord.totalCost)
# print(ord.printTotal)
