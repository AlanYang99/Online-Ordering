import pickle
class Food:
    '''
    Utility class for ingredients or food in general, which has the
    attributes: name, price, amount
    '''
    def __init__(self,name,price,amount):
        self._name = name
        self._price = price
        self._amount = amount

    def __str__(self):
        return f'{self._name}'

class inventory:

    @staticmethod
    def get_ingredients():
        infile = open("ingredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def addingredients(name,price,amount):
        infile = open("ingredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(item(name,price,amount))
        outfile = open("ingredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def get_burgerIngredients():
        infile = open("burgerIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def addburgerIngredients(name,price,amount):
        infile = open("burgerIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(item(name,price,amount))
        outfile = open("burgerIngredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def get_wrapIngredients():
        infile = open("wrapIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def addwrapIngredients(name,price,amount):
        infile = open("wrapIngredients",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(item(name,price,amount))
        outfile = open("wrapIngredients","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def get_sides():
        infile = open("sides",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def addsides(name,price,amount):
        infile = open("sides",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(item(name,price,amount))
        outfile = open("sides","wb")
        pickle.dump(inventory,outfile)
        outfile.close()

    @staticmethod
    def get_drinks():
        infile = open("drinks",'rb')
        inventory = pickle.load(infile)
        infile.close()
        return inventory

    @staticmethod
    def adddrinks(name,price,amount):
        infile = open("drinks",'rb')
        inventory = pickle.load(infile)
        infile.close()
        inventory.append(item(name,price,amount))
        outfile = open("drinks","wb")
        pickle.dump(inventory,outfile)
        outfile.close()
