from mains3 import Ingredients
from mains3 import Buns
from mains3 import Vegetables
from mains3 import Cheese
from mains3 import Sauce
from mains3 import Patties
from mains3 import strips
from mains3 import Buns
from mains3 import wraps
from mains3 import mains
from mains3 import Burgers
from mains3 import Wraps
from mains3 import meals
from sides1 import sides
from drinks import drinks
class food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount


class Order:
    #operates in the same way as booking
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__ (self, mains,sides, drinks):
        self._mains = mains
        self._sides = sides
        self._drinks = drinks

    def totalCost(self):
        price = 0
        price += self._mains.price()
        price += self._sides.printprice()
        price += self._drinks.price()
        return price

    def printTotal(self):
        output = ''
        output += self._mains.displayMains()
        output += self._drinks.printDrinks()
        output += self._sides.getSides()
        return output

Veg1 = Vegetables(1,2)
Cheese1 = Cheese(1,2)
Sauce1 = Sauce(1,2)
Patties1 = Patties(1,2)
Buns1 = Buns(1,2)
tender1 = strips(1,2)
wraps1 = wraps(1,2)

#print(help(Veg1))
Veg1.addIngredients('Pumpkin',0.4)
Veg1.setIngredients('Pumpkin',3)

Burger1 = Burgers(Veg1,Cheese1,Sauce1,Patties1,Buns1)
Wrap1 = Wraps(Veg1,Cheese1,Sauce1,tender1,wraps1)

meal1 = meals()
meal1.addBurger(Burger1)
meal1.addWrap(Wrap1)

drink1 = drinks()
drink1.set_cans('coke',2)
drink1.set_bottles('fanta',3)

side1 = sides()
side1.set_small_Fries(3)
side1.set_medium_fries(1)
side1.set_six_nuggets(4)
side1.set_other_sides('sundae',4)

order1 = Order(meal1,side1,drink1)
print(order1.printTotal())
print(order1.totalCost())
