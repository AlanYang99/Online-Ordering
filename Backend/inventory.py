import pickle

class Food:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.amount = amount

class Inventory:

    infile = open("test", "rb")
    ingredients = pickle.load(infile)
    infile.close()


    

    @classmethod
    def addIngredients(cls,name,price,amount):
        infile = open("test", "rb")
        ingredients = pickle.load(infile)
        ingredients.append(Food(name, 2, 3))
        infile.close()
        outfile = open("test", "wb")
        pickle.dump(ingredients, outfile)
        outfile.close()

    @classmethod
    def viewList(cls):
        infile = open("test","rb")
        cls.ingrediens1 = pickle.load(infile)
        infile.close()
        outfile = open("test", "wb")
        return cls.ingrediens1

Inventory.addIngredients("cat",2,1)
print(Inventory.viewList()[0].name)
