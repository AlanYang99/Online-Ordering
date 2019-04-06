from inventory import *

class Order:
    #operates in the same way as booking 
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__(self, buns, wraps, patties, ingredients, sides, drinks):
        self.buns = buns
        self.wraps = wraps
        self.patties = patties
        self.ingredients = ingredients
        self.sides = sides
        self.drinks = drinks