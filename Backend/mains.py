from abc import ABC

class ingredients:
    """
    Creates an ingredient object, which specifies the quantity
    of lettuce,cheese, onions for a main
    """
    def __init__(self):
        self._lettuce = 0
        self._cheese = 0
        self._tomato = 0
        self._onions = 0
        self._pickles = 0
        self._bacon - 0

    #Setter functions
    def numLettuce(self,lettuce):
        self._lettuce = lettuce

    def numCheese(self, cheese):
        self._cheese = cheese

    def numTomatoes(self,tomato):
        self._tomato = tomato

    def numOnions(self,onion):
        self._onions = onions

    def numPickles(self,pickles):
        self._pickles = pickles

    def numBacon(self, bacon):
        self._bacon - bacon

    #Getter functions
    @property
    def getIngredients(self):
        output = ''
        if(self._lettuce != 0):
            output += f'    Lettuce : {self._lettuce}\n'
        if(self._cheese != 0):
            output += f'    Cheese : {self._cheese}\n'
        if(self._tomato != 0):
            output += f'    Tomato : {self._tomato}\n'
        if(self._bacon != 0):
            output += f'    Bacon : {self._bacon}\n'
        if(self._onions != 0):
            output += f'    Onions : {self._onions}\n'
        if(self._pickles != 0):
            output += f'    Pickles : {self._pickles}\n'
        return output

    @property
    def getPrice(self):
        return 0 #Think of price later


class Sauce:

    """
    Creates a sauce object, which specifies which sauce
    the customer wants in their main
    """
    def __init__(self):
        self._tomatoSauce = 0
        self._BBqSauce = 0
        self._mayo = 0
        self._chilli_sauce = 0

    def numTomatoSauce(self,tomato_sauce):
        self._tomato_sauce = tomato_sauce

    def numBbqSauce(self, bbq_sauce):
        self._bbq_sauce = bbq_sauce

    def numMayo(self,mayo):
        self._mayo = mayo

    def numChilliSauce(self,chilli_sauce):
        self._chilli_sauce = chilli_sauce

    @property
    def getSauce(self):
        output = f'Sauce:'
        if(self._tomato_sauce is not 0):
            output+= f' Tomato Sauce'
        if(self._BBqSauce is not 0):
            output+= f' BBq Sauce'
        if(self._mayo is not 0):
            output+= f' Mayo Sauce'
        if(self._chilli_sauce is not 0):
            output+= f' Chilli Sauce'
        return output


class meat:
    def __init__(self):
        self._beef_patty = 0
        self._chick_fillet = 0
        self._crispy_chick = 0
        self._chick_tender = 0

    def numBeefPatty(self,beef_patty):
        self._beef_patty = beef_patty

    def numChickFillet(self, chick_fillet):
        self._chick_fillet = chick_fillet

    def numCrispyChick(self,crispy_chicken):
        self._crispy_chick = crispy_chicken

    def numOnions(self,_chick_tender):
        self._chick_tender = chick_tender


class Buns:

    def __init__(self):
        self._sesame_buns = 0
        self._muffin_buns = 0
        self._plain_bun = 0

    def numSesameBuns(self,sesame_bun):
        self._sesame_buns = sesame_bun

    def numMuffinBuns(self,muffin_bun):
        self._muffin_buns = muffin_bun

    def numPlainBuns(self,plain_bun):
        self._plain_bun = plain_bun
        

class Mains(ABC):

    def __init__(self,ingredients,sauce,meat):
        self._ingredients = ingredient
        self._sauce = sauce
        self._meat = meat

class Wraps(Mains):

    def __init__(self,ingredients,sauce,meat,wraps):
        Mains.__init__(ingredients,sauce,meat)
        self.wraps = wraps

    def wrapType(self,wraps):
        self._wrap = wraps


class Burgers(Mains):
    def __init__(self,ingredients,sauce,meat,buns):
        Mains.__init__(ingredients,sauce,meat)
        self.wraps = buns
