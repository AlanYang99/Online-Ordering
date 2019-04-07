from abc import ABC
from inventory import *

class Food:

    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount
        #self.category = category 

    def __str__(self):
        return f'{self.name} : {self.amount}\n'

class Ingredients():
    
    def __init__(self):
        self._ingredients = []

    def addIngredients(self,ingredient,price): #move to system.py supposed to be for staff to add new ingredients
        self._ingredients.append(Food(ingredient, price, 0))

    def setIngredients(self,ingredient,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is ingredient):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")
    #make price 2 decimal places at max to avoid
    #3.0000000000000000004
    def getPrice(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def getIngredients(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
        return output


    # @classmethod
    # def printSauce(cls):
    #     print(cls.ingredient[0])
    #     print(cls.ingredient[1])

#Can create another class similar to food, but amount is simply (less,normal,extra)
#cause 2 lettuce sounds weird
#ingredients = [Food('Lettuce', 1, 0), Food('Tomato', 1, 0), Food('Cheese', 1, 0), Food('Onion', 1, 0), Food('Tomato Sauce', 1, 0), Food('Barbecue Sauce', 1, 0)]

class Patties(Ingredients):

    def __init__(self,beef = 0,chicken = 0):
        self._ingredients = [Food('beefpatty',0.5, beef),Food('chickenpatty', 0.3, chicken)]

class strips(Ingredients):

    def __init__(self,chickentender = 0,grilledchicken = 0):
        self._ingredients = [Food('chickentender', 0.5, chickentender),Food('grilledchicken', 0.3, grilledchicken)]

class Buns(Ingredients):

    def __init__(self,sesame = 0,muffin = 0):
        self._ingredients = [Food('sesamebun',0.5, sesame),Food('muffinbun',0.3, muffin)]

class wraps(Ingredients):

    def __init__(self,tortilla = 0,flatbread = 0):
        self._ingredients = [Food('tortillawrap', 0.5, tortilla),Food('flatbread',0.3, flatbread)]

class mains(ABC):

    def __init__(self, Ingredients = None):
        self._ingredients = Ingredients

class Burgers(mains):

    def __init__(self,Ingredients = None,patties = None,Buns = None):
        super().__init__(Ingredients)
        self._buns = Buns
        self._patties = patties

    def getPrice(self):
        price = 0
        price += self._ingredients.getPrice()
        price += self._patties.getPrice()
        price += self._buns.getPrice()
        return round(price,2)

    def getIngredients(self):
        output = ''
        output += self._ingredients.getIngredients()
        output += self._patties.getIngredients()
        output += self._buns.getIngredients()
        return output

class Wraps(mains):

    def __init__(self,Ingredients = None, Strips = None, Wraps = None):
        super().__init__(Ingredients)
        self._wraps = Wraps
        self._strips = Strips

    def getPrice(self):
        price = 0
        price += self._ingredients.getPrice()
        price += self._strips.getPrice()
        price += self._wraps.getPrice()
        return round(price,2)

    def getIngredients(self):
        output = ''
        output += self._ingredients.getIngredients()
        output += self._strips.getIngredients()
        output += self._wraps.getIngredients()
        return output

class meals:

    def __init__(self):
        self._burgers = []
        self._wraps = []

    def addBurger(self,burger):
        self._burgers.append(burger)

    def addWrap(self,wrap):
        self._wraps.append(wrap)

    def displayMains(self):
        output = ''
        for i in self._burgers:
            output+= 'Plain burger:\n'
            output+= f' {i.getIngredients()}'
        for i in self._wraps:
            output+= 'Plain wrap:\n'
            output+= f' {i.getIngredients()}'
        return output

    def price(self):
        price = 0
        for i in self._burgers:
            price += i.getPrice()
        for i in self._wraps:
            price += i.getPrice()
        return price

# Veg1 = Vegetables(1,2)
# Cheese1 = Cheese(1,2)
# Sauce1 = Sauce(1,2)
# ings = Ingredients()
# ings.addIngredients('Lettuce', 1)
# ings.addIngredients('Tomato', 1)
# ings.addIngredients('Onion', 1)
# ings.setIngredients('Tomato', 3)


# Patties1 = Patties(1,2)
# Buns1 = Buns(1,2)
# tender1 = strips(1,2)
# wraps1 = wraps(1,2)
# print()
# burger1 = Burgers(ings,Patties1, Buns1)
# wrap1 = Wraps(ings, tender1, wraps1)

# meal = meals()
# meal.addBurger(burger1)
# meal.addWrap(wrap1)


# print(burger1.getIngredients())
# print(burger1.getPrice())
# print(wrap1.getIngredients())
# print(wrap1.getPrice())
# print(meal.displayMains())
# print(meal.price())

#print(help(Veg1))
#Veg1.addIngredients('Pumpkin',0.4)
#Veg1.setIngredients('Pumpkin',3)

#Burger1 = Burgers(Veg1,Cheese1,Sauce1,Patties1,Buns1)
#Wrap1 = Wraps(Veg1,Cheese1,Sauce1,tender1,wraps1)
"""
print(Burger1.getIngredients())
print('Price = ')
print(Burger1.getPrice()

print(Wrap1.getIngredients())
print('Price = ')
print(Wrap1.getPrice())

meal1 = meals()
meal1.addBurger(Burger1)
meal1.addWrap(Wrap1)
print(meal1.displayMains())
print(meal1.price())
"""