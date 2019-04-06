from abc import ABC
from enum1 import addOns
from enum1 import Buns
from enum1 import patties
from enum1 import Sauce

class ingredients():
    """
    Creates an ingredient object, which specifies the quantity
    of lettuce,cheese, onions for a main
    """

    ingredients1 = {
        "choi fan" : 1,
        "bok choy" : 2,
        "Funny" : 4
    }
    def __init__(self):
        self.lettuce = 0
        self.cheese = 0
        self.tomato = 0
        self.onions = 0
        self.pickles = 0
        self.bacon = 0

    self.ingredients = ingredients1

    def printIngredients(self):
        for i in self.ingredients:
            print(i)
"""
    def setIngredient(self,addon,amount)
        for i in addOns:
            y = str(i).split('.')
            if(addon == y[1]):


    def setIngredient(self,addOn):
        member = addOns(1)
"""

print(isinstance(str(addOns(1)),str))
print(str(addOns(1)))
y,x = str(addOns(1)).split('.')
print(x)
print(isinstance(x,str))
for i in addOns:
    print(i)

q = ingredients()
