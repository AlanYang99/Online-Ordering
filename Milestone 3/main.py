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
class WrapIngredients():

    def __init__(self):
        self._wrap_ingredients = []

    def set_wrap_ingredients(self,wrap_ingredient,amount):
        found = 0
        infile = open("wrapIngredients", "rb")
        wrap_ingredients = pickle.load(infile)
        infile.close()
        for i in wrap_ingredients:
            if(i._name == wrap_ingredient):
                self._wrap_ingredients.append(Food(i._name, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Ingredient is not found")

    @property
    def get_wrap_ingredients(self):
        wrap_ingredient_list = ' '
        for ingredient in self._wrap_ingredients:
            wrap_ingredient_list += "   " + str(ingredient)
        return wrap_ingredient_list

    @property
    def price(self):
        cost = 0
        for ingredient in self._wrap_ingredients:
            cost += (ingredient._amount * ingredient._price)
        return cost

class BurgerIngredients():

    def __init__(self):
        self._burger_ingredients = []

    def set_burger_ingredients(self,burger_ingredient,amount):
        found = 0
        infile = open("burgerIngredients", "rb")
        burger_ingredients = pickle.load(infile)
        infile.close()
        for i in burger_ingredients:
            if(i._name == burger_ingredient):
                self._burger_ingredients.append(Food(i._name, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Ingredient is not found")

    @property
    def get_burger_ingredients(self):
        burger_ingredient_list = ' '
        for ingredient in self._burger_ingredients:
            burger_ingredient_list += "   " + str(ingredient)
        return burger_ingredient_list

    @property
    def price(self):
        cost = 0
        for ingredient in self._burger_ingredients:
            cost += (ingredient._amount * ingredient._price)
        return cost

class Mains(ABC):

    def __init__(self,ingredient):
        self._ingredients = ingredient

class Burgers(Mains):

    def __init__(self,ingredients = None,burger_ingredients = None,amount = 0):
        super().__init__(ingredients)
        self._burger_ingredients = burger_ingredients
        self._amount = amount #The amount of burgers a customer has orderd
                              #with the same product

    @property
    def price(self):
        price = 0
        if(self._ingredients != None):
            price += self._ingredients.price
        if(self._burger_ingredients != None):
            price += self._burger_ingredients.price
        price*= int(self._amount)
        return (round(price,2))

    @property
    def get_ingredients(self):
        output = ''
        if(self._ingredients != None):
            output += self._ingredients.get_ingredients
        if(self._burger_ingredients != None):
            output += self._burger_ingredients.get_burger_ingredients
        return output



class Wraps(Mains):

    def __init__(self,ingredients = None,wrap_ingredients = None,amount = 0):
        super().__init__(ingredients)
        self._wrap_ingredients = wrap_ingredients
        self._amount = amount

    @property
    def price(self):
        price = 0
        price += self._ingredients.price
        price += self._wrap_ingredients.price
        price *= int(self._amount)
        return round(price,2)

    @property
    def get_ingredients(self):
        output = ''
        output += self._ingredients.get_ingredients
        output += self._wrap_ingredients.get_wrap_ingredients
        return output

class Meals:

    ingr1 = Ingredients()
    ingr1.set_ingredients('Tomato Slices',2)
    ingr1.set_ingredients('Cheddar Cheese',1)
    ingr1.set_ingredients('Lettuce',2)
    ingr1.set_ingredients('Hot Sauce',1)

    burg1 = BurgerIngredients()
    burg1.set_burger_ingredients('Sesame Seed Bun',2)
    burg1.set_burger_ingredients('Beef Patty',2)

    wrap1 = WrapIngredients()
    wrap1.set_wrap_ingredients('Lavash',2)
    def __init__(self):
        self._burgers = []
        self._wraps = []
        self._Luger_Burger = Burgers(Meals.ingr1,Meals.burg1,1)
        self._Luger_Wrap = Wraps(Meals.ingr1,Meals.wrap1,1)


    def add_burger(self,burger):
        self._burgers.append(burger)

    def add_wrap(self,wrap):
        self._wraps.append(wrap)

    def add_Luger_Burger(self,amount):
        to_add = Burgers(Meals.ingr1,Meals.burg1,amount)
        self._burgers.append(to_add)

    def add_Luger_Wrap(self,amount):
        to_add = wraps(Meals.ingr1,Meals.wrap1,amount)
        self._wraps.append(to_add)

    @property
    def display_mains(self):
        output = ''
        for i in self._burgers:
            output+= f'{i._amount}x Plain burger:\n'
            output+= f' {i.get_ingredients}'
        for i in self._wraps:
            output+= f'{i._amount}x Plain wrap:\n'
            output+= f' {i.get_ingredients}'
        return output

    @property
    def price(self):
        price = 0
        for i in self._burgers:
            price += i.price
        for i in self._wraps:
            price += i.price
        return price
