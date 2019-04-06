from abc import ABC

class Food:

    def __init__(self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price

class Ingredients:
    """
    Creates an ingredient object, that consists of how many addOns
    a main has
    """

    def __init__(self):
        self._ingredients = []

    def addIngredients(self,ingredient,amount)
