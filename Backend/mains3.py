
class Food:

    def __init__(self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price

    def __str__(self):
        return f'{self.name} : {self.amount}'

class Ingredients():


    def addIngredients(self,ingredient,price):
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

class Cheese:

    def __init__(self,cheddar = 0,feta = 0):
        self._ingredients = [Food('cheddarcheese',cheddar,0.5),Food('fetacheese',feta,0.3)]

class Sauce:

    def __init__(self,tomato = 0,bbq = 0):
        self._ingredients = [Food('tomatosauce',tomato,0.5),Food('bbqsauce',bbq,0.3)]

class patties:

    def __init__(self,beef = 0,chicken = 0):
        self._ingredients = [Food('beefpatty',tomato,0.5),Food('chickenpatty',bbq,0.3)]

class buns:

    def __init__(self,sesame = 0,muffin = 0):
        self._ingredients = [Food('sesamebun',sesame,0.5),Food('muffinbun',muffin,0.3)]


Veg1 = Vegetables(1,2)
#print(help(Veg1))
print(Veg1.getIngredients())
print(Veg1.getPrice())
Veg1.addIngredients('Pumpkin',0.4)
Veg1.setIngredients('Pumpkin',3)
print(Veg1.getIngredients())
print(Veg1.getPrice())
