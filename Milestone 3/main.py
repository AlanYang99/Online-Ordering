from abc import ABC
from src.inventory import Food
import dill as pickle

# class Food:
#     '''
#     Utility class for ingredients or food in general, which has the
#     attributes: name, price, amount
#     '''
#     def __init__(self,name,price,amount):
#         self._name = name
#         self._price = price
#         self._amount = amount
#
#     #Changes the str function
#     def __str__(self):
#         if(self._amount is not 0):
#             return f'{self._amount} x {self._name} : {self._price * self._amount}'

class Ingredients():
    '''
    Ingredients class which contains an attribute which is a list of
    items
    '''
    #Inventory should retrive from the actual inventory class
    #to see avaiable items

    def __init__(self):
        self._ingredients = []

    '''
    Passes in a string (ingredient name), and checks if that
    ingredient exist in the system, if it does allows customer
    to choose the amount they want to order
    '''
    def set_ingredients(self,ingredient,amount):
        found = 0
        infile = open("Ingredients", "rb")
        ingredients = pickle.load(infile)
        infile.close()
        for i in ingredients:
            if(i._name == ingredient):
                self._ingredients.append(Food(ingredient, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Ingredient is not found")

    @property
    def get_ingredients(self):
        ingredient_list = ' '
        for ingredient in self._ingredients:
            ingredient_list += "   " + str(ingredient)
        return ingredient_list

    @property
    def price(self):
        cost = 0
        for ingredient in self._ingredients:
            cost += (ingredient._amount * ingredient._price)
        return cost

#Could just name wrapIngredients and burgeringredients as ingredients and just
#inherit from Ingredients
class WrapIngredients:

    def __init__(self):
        self._wrapIngredients = []

    def set_wrap_ingredients(self,wrapIngredient,amount):
        found = 0
        infile = open("wrapIngredients", "rb")
        wrapIngredients = pickle.load(infile)
        infile.close()
        for i in wrapIngredients:
            if(i._name == wrapIngredient):
                self._wrapIngredients.append(Food(i._name, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Ingredient is not found")

    @property
    def get_wrap_ingredients(self):
        wrap_ingredient_list = ' '
        for ingredient in self._wrapIngredients:
            wrap_ingredient_list += "   " + str(ingredient)
        return wrap_ingredient_list

    @property
    def price(self):
        cost = 0
        for ingredient in self._wrapIngredients:
            cost += (ingredient._amount * ingredient._price)
        return cost

class BurgerIngredients:

    def __init__(self):
        self._burgerIngredients = []

    def set_burger_ingredients(self,burgerIngredient,amount):
        found = 0
        infile = open("burgerIngredients", "rb")
        burgerIngredients = pickle.load(infile)
        infile.close()
        for i in burgerIngredients:
            if(i._name == burgerIngredient):
                self._burgerIngredients.append(Food(i._name, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Ingredient is not found")

    @property
    def get_burger_ingredients(self):
        burger_ingredient_list = ' '
        for ingredient in self._burgerIngredients:
            burger_ingredient_list += "   " + str(ingredient)
        return burger_ingredient_list

    @property
    def price(self):
        cost = 0
        for ingredient in self._burgerIngredients:
            cost += (ingredient._amount * ingredient._price)
        return cost

class Mains(ABC):

    def __init__(self,ingredient):
        self._ingredients = ingredient

class Burgers(Mains):

    def __init__(self,ingredients = None,burgerIngredients = None):
        super().__init__(ingredients)
        self._burgerIngredients = burgerIngredients

    @property
    def price(self):
        price = 0
        price += self._ingredients.price
        price += self._burgerIngredients.price
        return round(price,2)

    @property
    def get_ingredients(self):
        output = ''
        output += self._ingredients.getIngredients
        output += self._burgerIngredients.get_burgerIngredients
        return output

class Wraps(Mains):

    def __init__(self,ingredients = None,wrapIngredients = None):
        super().__init__(ingredients)
        self._wrapIngredients = wrapIngredients

    @property
    def price(self):
        price = 0
        price += self._ingredients.price
        price += self._wrapIngredients.price
        return round(price,2)

    @property
    def get_ingredients(self):
        output = ''
        output += self._ingredients.getIngredients
        output += self._wrapIngredients.get_wrapIngredients
        return output

class Meals:

    def __init__(self):
        self._burgers = []
        self._wraps = []

    def add_burger(self,burger):
        self._burgers.append(burger)

    def add_wrap(self,wrap):
        self._wraps.append(wrap)

    @property
    def display_mains(self):
        output = ''
        for i in self._burgers:
            output+= 'Plain burger:\n'
            output+= f' {i.getIngredients}'
        for i in self._wraps:
            output+= 'Plain wrap:\n'
            output+= f' {i.getIngredients}'
        return output

    @property
    def price(self):
        price = 0
        for i in self._burgers:
            price += i.price
        for i in self._wraps:
            price += i.price
        return price