import pickle
import datetime
from order import *
from main import *
from inventory import Food

class OrderID:

    id_generator = 1

    def __init__(self,order): #Not sure if we need status tbh
                                    #When the order is created, the status should begin ('In preparation')
        self._order = order
        self._status = 'In preparation'
        self._id = id_generator #This part needs some changing, because we are going to
        self._time = datetime.datetime.now()
        id_generator +=1
                              #method that updates order1
                                #Just think about it this way, there may be 2 identical ids
    def update_status(self,status):
        self._status = status

class Orders:

    def __init__(self):
        self._orders = []

    def delete_order(self,id):
        for order in self._orders:
            if order._id is order:
                self._orders.remove(order)

    def get_order(self,id):
        for order in self._orders:
            if order._id is order:
                return order
        return None

    def make_order(self,mains,sides,drinks):

        #Checking if available ingredients 1st
        new_order = Order(mains,sides,drinks)
        self._orders.append(new_order)

def add_ingredients(name,price,amount,ingredient_type):
    infile = open(ingredient_type,'rb')
    inventory = pickle.load(infile)
    infile.close()
    inventory.append(Food(name,price,amount))
    outfile = open(ingredient_type,"wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_ingredients(name,amount):
    infile = open("Ingredients",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name is name):
            i._amount += amount
    outfile = open("Ingredients","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_wraps_ingredients(name,amount):
    infile = open("wrapIngredients",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name is name):
            i._amount += amount
    outfile = open("wrapIngredients","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_burger_ingredients(name,amount):
    infile = open("burgerIngredients",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name is name):
            i._amount += amount
    outfile = open("burgerIngredients","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_sides(name,amount):
    infile = open("sides",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name is name):
            i._amount += amount
    outfile = open("sides","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_drinks(name,amount):
    infile = open("drinks",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name is name):
            i._amount += amount
    outfile = open("drinks","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

# add_ingredients("Fries",1,2000,"sides")
# add_ingredients("Nuggets",1,2000,"sides")
# add_ingredients("Soft Serve",0.5,1500,"sides")
# add_ingredients("Strawberry Sundae",2,800,"sides")
# add_ingredients("Chocolate Sundae",2,800,"sides")
# add_ingredients("Caramel Sundae",2,800,"sides")
# add_ingredients("Hash Brown",1.2,500,"sides")
# add_ingredients("Salad",2.5,1000,"sides")
# add_ingredients("Coca Cola Can",1.1,1500,"drinks")
# add_ingredients("Fanta Can",1.1,1500,"drinks")
# add_ingredients("Solo Can",1.1,1500,"drinks")
# add_ingredients("Coca Cola Bottle",2,1500,"drinks")
# add_ingredients("Fanta Bottle",2,1500,"drinks")
# add_ingredients("Solo Bottle",2,1500,"drinks")
# add_ingredients("Large Boba",6,100000,"drinks")
# add_ingredients("Frozen Coke",1,2000,"drinks")
# add_ingredients("Frozen Fanta",1,2000,"drinks")
# add_ingredients("Vanilla Milkshake",2.5,500,"drinks")
# add_ingredients("Chocolate Milkshake",2.5,500,"drinks")
# add_ingredients("Strawberry Milkshake",2.5,500,"drinks")

# add_ingredients("Medium Fries",2,400,"sides")
# add_ingredients("Large Fries",2,400,"sides")
# add_ingredients("10-pack Nuggets",2.5,200,"sides")
