from abc import ABC

class item:
    '''
    Utility class for ingredients or food in general, which has the
    attributes: name, price, amount
    '''
    def __init__(self,name,price,amount,type):
        self._name = name
        self._price = price
        self._amount = amount
        self._type = type

    #Changes the str function
    def __str__(self):
        if(self._amount is not 0):
            return f'{self._amount} x {self._name} : {self._price * self._amount}'

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
        infile = open("ingredients", "rb")
        ingredients = pickle.load(infile)
        infile.close()
        for i in ingredients:
            if(i.name is ingredient):
                self._ingredients.append(Food(i._name, i._price, i._amount))
                found = 1
        if(found is 0):
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
class wrapIngredients:

    Inventory = []

    def __init__(self):
        self._wrapIngredients = []

    def set_wrapIngredients(self,wrapIngredient,amount):
        found = 0
        infile = open("wrapIngredients", "rb")
        wrapIngredients = pickle.load(infile)
        infile.close()
        for i in wrapIngredients:
            if(i._name is wrapIngredient):
                self._wrapIngredients.append(Food(i._name, i._price, i._amount))
                found = 1
        if(found is 0):
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

class burgerIngredients:

    Inventory = []

    def __init__(self):
        self._burgerIngredients = []

    def set_burgerIngredients(self,burgerIngredient,amount):
        found = 0
        infile = open("burgerIngredients", "rb")
        burgerIngredients = pickle.load(infile)
        infile.close
        for i in burgerIngredients:
            if(i._name is burgerIngredient):
                self._burgerIngredients.append(Food(i._name, i._price, i._amount))
                found = 1
        if(found is 0):
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

class burgers(ABC):
