from abc import ABC

class ingredients:
    """
    Creates an ingredient object, which shows how much addOns (cheese,
    bacon,lettuce,etc) a main has
    """

    def __init__(self):
        self._ingredients = {
            'lettuce' : 0,
            'cheese' : 0,
            'tomatoes' : 0,
            'onions' : 0,
            'bacon' : 0,
            'pickles' : 0
        }

    def addIngredients(self,ingredient,amount):
        addOn = ingredient.tolower()
        if addOn in self._ingredients:
            self._ingredients[addOn] = amount
        else:
            print("Ingredient doesnt exist")

class sauce:
    """
    Creates an ingredient object, which shows how much addOns (cheese,
    bacon,lettuce,etc) a main has
    """

    def __init__(self):
        self._sauces = {
            'tomato sauce' : 0,
            'bbq sauce' : 0,
            'mayo' : 0,
            'chilli sauce' : 0
        }

    def addSauce(self,Sauce,amount):
        sauce = Sauce.tolower()
        if addOn in self._sauces:
            self._sauces[sauce] = amount
        else:
            print("Ingredient doesnt exist")

class meat:
    """
    Creates an ingredient object, which shows how much addOns (cheese,
    bacon,lettuce,etc) a main has
    """

    def __init__(self):
        self._meats = {
            'beaf patty' : 0,
            'chicken fillet' : 0,
            'crispy chicken' : 0,
            'chicken tender' : 0
        }

    def addMeat(self,Meat,amount):
        meat = Meat.tolower()
        if meat in self._meats:
            self._meats[meat] = amount
        else:
            print("Ingredient doesnt exist")

class Buns:
    def __init__(self):
        self._buns = {
            'sesame buns' = 0,
            'muffind buns' = 0,
            'plain buns' = 0
        }

class mains(ABC):

    def __init__(self,ingredients,sauce,meat):
        self._ingreidents = ingredients
        self._sauce = sauce
        self._meat = meat



    #Create setter functions

class Wraps(Mains):
    pass
    ## TODO:

class Burgers(Main):
    pass
    ## TODO:
