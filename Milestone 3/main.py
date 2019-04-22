from abc import ABC
from inventory import Food
import pickle

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
        infile = open("Ingredients1", "rb")
        ingredients1 = pickle.load(infile)
        infile.close()
        for i in ingredients:
            if(i._name == ingredient):
                self._ingredients.append(Food(ingredient, i._price, amount))
                found = 1

        for i in ingredients1:
            if(i._name == ingredient):
                self._ingredients.append(Food(ingredient, i._price, amount))
                found = 1
        if(found == 0):
            print("Ingredient is not found")

    @property
    def getIngredients(self):
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
class wrapIngredients():

    def __init__(self):
        self._wrapIngredients = []

    def set_wrapIngredients(self,wrapIngredient,amount):
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
    def get_wrapIngredients(self):
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

class burgerIngredients():

    def __init__(self):
        self._burgerIngredients = []

    def set_burgerIngredients(self,burgerIngredient,amount):
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
    def get_burgerIngredients(self):
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

class mains(ABC):

    def __init__(self,ingredient):
        self._ingredients = ingredient

class burgers(mains):

    def __init__(self,ingredients = None,burgerIngredients = None,amount = 0):
        super().__init__(ingredients)
        self._burgerIngredients = burgerIngredients
        self._amount = amount #The amount of burgers a customer has orderd
                              #with the same product

    @property
    def price(self):
        price = 0
        print(price)
        if(self._ingredients != None):
            price += self._ingredients.price
            print(price)
        if(self._burgerIngredients != None):
            price += self._burgerIngredients.price
            print(price)
        price*= int(self._amount)
        return (round(price,2))

    @property
    def getIngredients(self):
        output = ''
        if(self._ingredients != None):
            output += self._ingredients.getIngredients
        if(self._burgerIngredients != None):
            output += self._burgerIngredients.get_burgerIngredients
        return output



class wraps(mains):

    def __init__(self,ingredients = None,wrapIngredients = None,amount = 0):
        super().__init__(ingredients)
        self._wrapIngredients = wrapIngredients
        self._amount = amount

    @property
    def price(self):
        price = 0
        price += self._ingredients.price
        price += self._wrapIngredients.price
        price *= int(self._amount)
        return round(price,2)

    @property
    def getIngredients(self):
        output = ''
        output += self._ingredients.getIngredients
        output += self._wrapIngredients.get_wrapIngredients
        return output

class meals:

    ingr1 = Ingredients()
    ingr1.set_ingredients('Tomato Slices',2)
    ingr1.set_ingredients('Cheddar Cheese',1)
    ingr1.set_ingredients('Lettuce',2)
    ingr1.set_ingredients('Hot Sauce',1)

    burg1 = burgerIngredients()
    burg1.set_burgerIngredients('Sesame Seed Bun',2)
    burg1.set_burgerIngredients('Beef Patty',2)

    wrap1 = wrapIngredients()
    wrap1.set_wrapIngredients('Lavash',2)
    def __init__(self):
        self._burgers = []
        self._wraps = []
        self._Luger_Burger = burgers(meals.ingr1,meals.burg1,1)
        self._Luger_Wrap = wraps(meals.ingr1,meals.wrap1,1)


    def addBurger(self,burger):
        self._burgers.append(burger)

    def addWrap(self,wrap):
        self._wraps.append(wrap)

    def add_Luger_Burger(self,amount):
        toAdd = burgers(meals.ingr1,meals.burg1,amount)
        self._burgers.append(toAdd)

    def add_Luger_Wrap(self,amount):
        toAdd = wraps(meals.ingr1,meals.wrap1,amount)
        self._wraps.append(toAdd)

    @property
    def displayMains(self):
        output = ''
        for i in self._burgers:
            output+= f'{i._amount}x Plain burger:\n'
            output+= f' {i.getIngredients}'
        for i in self._wraps:
            output+= f'{i._amount}x Plain wrap:\n'
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
