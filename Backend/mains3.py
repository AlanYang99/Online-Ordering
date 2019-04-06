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

    def __init__(self,lettuce = 0,tomato = 0): #lettuce and tomato should be ints
        #self._lettuce = Food('lettuce',lettuce,0.5) #50cents per serving of lettuce
        #self._tomato = Food('tomatoes',tomato,0.3)
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



    @property
    def lettuce(self):
        return self._lettuce.amount

    @property
    def tomato(self):
        return self._tomato.amount

    def setLettuce(self,amount):
        self._lettuce.amount = amount

    def setTomato(self,amount):
        self._tomato.amount = amount

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


Veg = Vegetables(1,1)
Veg.addIngredients('Pumpkin',0.6) #Assuming staff added new item
Veg.setIngredients('Pumpkin',4) #Customer orders 4 serving of pumpkin
print(Veg.getVegetables())
