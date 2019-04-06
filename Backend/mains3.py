class Food:

    def __init__(self,name,amount,price):
        self.name = name
        self.amount = amount
        self.price = price

    def __str__(self):
        return f'{self.name} : {self.amount}'

#Can create another class similar to food, but amount is simply (less,normal,extra)
#cause 2 lettuce sounds weird

class Vegetables:

    def __init__(self,lettuce = 0,tomato = 0):
        self._ingredients = [Food('lettuce',lettuce,0.5),Food('tomatoes',tomato,0.3)]

    def addIngredients(self,vege,price):
        self._ingredients.append(Food(vege,0,price))

    def setIngredients(self,vege,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is vege):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")

    def getPrice(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def getVegetables(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
            output += '\n'
        return output

class Cheese:

    def __init__(self,cheddar = 0,feta = 0):
        self._ingredients = [Food('cheddarcheese',cheddar,0.5),Food('fetacheese',feta,0.3)]

    def addIngredients(self,cheese,price):
        self._ingredients.append(Food(cheese,0,price))

    def setIngredients(self,cheese,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is cheese):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")

    def get_price(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def get_cheese(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
            output += '\n'
        return output

class Sauce:

    def __init__(self,tomato = 0,bbq = 0):
        self._ingredients = [Food('tomatosauce',tomato,0.5),Food('bbqsauce',bbq,0.3)]

    def addIngredients(self,cheese,price):
        self._ingredients.append(Food(sauce,0,price))

    def setIngredients(self,sauce,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is sauce):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")

    def get_price(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def get_sauce(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
            output += '\n'
        return output

class patties:

    def __init__(self,beef = 0,chicken = 0):
        self._ingredients = [Food('beefpatty',tomato,0.5),Food('chickenpatty',bbq,0.3)]

    def addIngredients(self,patty,price):
        self._ingredients.append(Food(patty,0,price))

    def setIngredients(self,patty,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is patty):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")

    def get_price(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def get_sauce(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
            output += '\n'
        return output

class buns:

    def __init__(self,sesame = 0,muffin = 0):
        self._ingredients = [Food('sesamebun',sesame,0.5),Food('muffinbun',muffin,0.3)]

    def addIngredients(self,bun,price):
        self._ingredients.append(Food(bun,0,price))

    def setIngredients(self,bun,amount):
        found = 0
        for i in self._ingredients:
            if(i.name is bun):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Ingredient not found")

    def get_price(self):
        cost = 0
        for i in self._ingredients:
            cost += i.amount * i.price
        return cost

    def get_sauce(self):
        output = ''
        for i in self._ingredients:
            output+= i.__str__()
            output += '\n'
        return output
