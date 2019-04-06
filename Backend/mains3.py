from abc import ABC
class Food:

    def __init__(self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price

    def __str__(self):
        return f'{self.name} : {self.amount}'

class Ingredients(ABC):

    def addIngredients(self,ingredient,price): #move to system.py supposed to be for staff to add new ingredients
        self._ingredients.append(Food(ingredient,0,price))

    def setIngredients(self,ingredient,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is ingredient):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")
    #make price 2 decimal places at max to avoid
    #3.0000000000000000004
    def getPrice(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def getIngredients(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
            output += '\n'
        return output
#Can create another class similar to food, but amount is simply (less,normal,extra)
#cause 2 lettuce sounds weird

class Vegetables(Ingredients):

    def __init__(self,lettuce = 0,tomato = 0):
        self._ingredients = [Food('lettuce',lettuce,0.5),Food('tomatoes',tomato,0.3)]

class Cheese(Ingredients):

    def __init__(self,cheddar = 0,feta = 0):
        self._ingredients = [Food('cheddarcheese',cheddar,0.5),Food('fetacheese',feta,0.3)]

class Sauce(Ingredients):

    def __init__(self,tomato = 0,bbq = 0):
        self._ingredients = [Food('tomatosauce',tomato,0.5),Food('bbqsauce',bbq,0.3)]

class Patties(Ingredients):

    def __init__(self,beef = 0,chicken = 0):
        self._ingredients = [Food('beefpatty',beef,0.5),Food('chickenpatty',chicken,0.3)]

class strips(Ingredients):

    def __init__(self,chickentender = 0,grilledchicken = 0):
        self._ingredients = [Food('chickentender',chickentender,0.5),Food('grilledchicken',grilledchicken,0.3)]

class Buns(Ingredients):

    def __init__(self,sesame = 0,muffin = 0):
        self._ingredients = [Food('sesamebun',sesame,0.5),Food('muffinbun',muffin,0.3)]

class wraps(Ingredients):

    def __init__(self,tortilla = 0,flatbread = 0):
        self._ingredients = [Food('tortillawrap',tortilla,0.5),Food('flatbread',flatbread,0.3)]

class mains(ABC):

    def __init__(self,vegetables,cheese,sauce):
        self._vegetables = vegetables
        self._cheese = cheese
        self._sauce = sauce

class Burgers(mains):

    def __init__(self,vegetables = None,cheese = None ,sauce = None,patties = None,buns = None):
        super().__init__(vegetables,cheese,sauce)
        self._patties = patties
        self._buns = buns

    def getPrice(self):
        price = 0
        price += self._vegetables.getPrice()
        price += self._cheese.getPrice()
        price += self._sauce.getPrice()
        price += self._patties.getPrice()
        price += self._buns.getPrice()
        return price

    def getIngredients(self):
        output = ''
        output += self._vegetables.getIngredients()
        output += self._cheese.getIngredients()
        output += self._sauce.getIngredients()
        output += self._patties.getIngredients()
        output += self._buns.getIngredients()
        return output

class Wraps(mains):

    def __init__(self,vegetables = None,cheese = None ,sauce = None,strips = None,wraps = None):
        super().__init__(vegetables,cheese,sauce)
        self._strips = strips
        self._wraps = wraps

    def getPrice(self):
        price = 0
        price += self._vegetables.getPrice()
        price += self._cheese.getPrice()
        price += self._sauce.getPrice()
        price += self._strips.getPrice()
        price += self._wraps.getPrice()
        return price

    def getIngredients(self):
        output = ''
        output += self._vegetables.getIngredients()
        output += self._cheese.getIngredients()
        output += self._sauce.getIngredients()
        output += self._strips.getIngredients()
        #output += self._wraps.getIngredients()
        return output

class meals:

    def __init__(self):
        self._burgers = []
        self._wraps = []

    def addBurger(self,burger):
        self._burgers.append(burger)

    def addWrap(self,wrap):
        self._wraps.append(wrap)

    def displayMains(self):
        output = ''
        for i in self._burgers:
            output+= 'Plain burger:\n'
            output+= f' {i.getIngredients()}'
        for i in self._wraps:
            output+= 'Plain wrap:\n'
            output+= f' {i.getIngredients()}'
        return output

    def price(self):
        price = 0
        for i in self._burgers:
            price += i.getPrice()
        for i in self._wraps:
            price += i.getPrice()
        return price

Veg1 = Vegetables(1,2)
Cheese1 = Cheese(1,2)
Sauce1 = Sauce(1,2)
Patties1 = Patties(1,2)
Buns1 = Buns(1,2)
tender1 = strips(1,2)
wraps1 = wraps(1,2)

#print(help(Veg1))
Veg1.addIngredients('Pumpkin',0.4)
Veg1.setIngredients('Pumpkin',3)

Burger1 = Burgers(Veg1,Cheese1,Sauce1,Patties1,Buns1)
Wrap1 = Wraps(Veg1,Cheese1,Sauce1,tender1,wraps1)
print(Burger1.getIngredients())
print('Price = ')
print(Burger1.getPrice())

print(Wrap1.getIngredients())
print('Price = ')
print(Wrap1.getPrice())

meal1 = meals()
meal1.addBurger(Burger1)
meal1.addWrap(Wrap1)
print(meal1.displayMains())
print(meal1.price())
