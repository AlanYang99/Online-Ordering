from inventory import *

class Order:
    #operates in the same way as booking 
    #takes in 3 parameters - drinks, mains, sides, self
    def __init__(self, buns, wraps, patties, ingredients, sides, drinks):
        self.buns = []
        self.wraps = []
        self.patties = []
        self.ingredients = []
        self.sides = []
        self.drinks = []