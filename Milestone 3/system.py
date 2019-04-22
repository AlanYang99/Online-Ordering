import pickle
import datetime
from order import *
from main import *
from inventory import Food
# from app import side1,drink1,meal1,order1

class OrderId:

    id_generator = 1
    def __init__(self, order):
        self._order = order
        self._id = OrderId.id_generator
        self._time = datetime.datetime.now()
        self._status = 'In preparation'
        OrderId.id_generator +=1

class OrderSystem:
    def __init__(self):
        self._orders = []  #for now, make a pickle file for orderlist

    def make_booking(self,order):
        new_order = OrderId(order)
        self._orders.append(new_order)
        return new_order

    def get_order(self,id):
        for order in self._orders:
            if(int(order._id) == int(id)):
                return order
        return None
        # for order in self._orders:
        #     if(order._id == int(id)):
        #         return order
        # return None
        # for order in self._orders:
        #     print("test3")
        #     print(order._order._sides._sides)
        #
        #     if(str(order._id) == str(id)):
        #         print("test4")
        #         print(order._order._sides._sides)
        #         return order
        # return None

    def delete_order(self,id):
        i = 0
        for order in self._orders:
            if(str(order._id) == str(id)):
                break
            i+=1
        del self._orders[i]

    def update_status(self,id):
        for order in self._orders:
            if(str(order._id) == str(id)):
                order._status = 'Ready to be collected'
        # global side1
        # global drink1
        # global order1
        # global meal1
        #
        # side1._sides = []
        # drink1._drinks = []
        # meal1._burgers = []
        # meal1._wraps = []
        # order1._sides = []
        # order1._mains = []
        # order1._drinks = []

sys = OrderSystem()


# class OrderID:
#
#     id_generator = 1
#
#     def __init__(self,order): #Not sure if we need status tbh
#                                     #When the order is created, the status should begin ('In preparation')
#         self._order = order
#         self._status = 'In preparation'
#         self._id = id_generator #This part needs some changing, because we are going to
#         self._time = datetime.datetime.now()
#         id_generator +=1
#                               #method that updates order1
#                                 #Just think about it this way, there may be 2 identical ids
#     def update_status(self,status):
#         self._status = status
#
# class OrderList:
#
#     def __init__(self):
#         self._orders = []
#
#     def deleteOrder(self,id):
#         for order in self._orders:
#             if order._id is order:
#                 self._orders.remove(order)
#
#     def getOrder(self,id):
#         for order in self._orders:
#             if order._id is order:
#                 return order
#         return None
#
#     def add_order(self,order):
#         self._orders.append(order)

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
    print(len(inventory))
    for i in inventory:
        if(i._name == name):
            i._amount += amount
            print(i._amount)
    outfile = open("Ingredients","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_ingredients1(name,amount):
    infile = open("Ingredients1",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name == name):
            i._amount += amount
    outfile = open("Ingredients1","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_wraps_ingredients(name,amount):
    infile = open("wrapIngredients",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name == name):
            i._amount += amount
    outfile = open("wrapIngredients","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_burger_ingredients(name,amount):
    infile = open("burgerIngredients",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name == name):
            i._amount += amount
    outfile = open("burgerIngredients","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_sides(name,amount):
    infile = open("sides",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name == name):
            i._amount += amount
    outfile = open("sides","wb")
    pickle.dump(inventory,outfile)
    outfile.close()

def increment_drinks(name,amount):
    infile = open("drinks",'rb')
    inventory = pickle.load(infile)
    infile.close()
    for i in inventory:
        if(i._name == name):
            i._amount += amount
    outfile = open("drinks","wb")
    pickle.dump(inventory,outfile)
    outfile.close()
# add_ingredients("Lettuce",0.3,2000,"Ingredients1")
# add_ingredients("Diced Tomatoes",0.2,2000,"Ingredients1")
# add_ingredients("Fried Onions",0.2,2000,"Ingredients1")
# add_ingredients("Pickles",0.2,2000,"Ingredients1")
# add_ingredients("Tomato Sauce",0.2,1500,"Ingredients1")
# add_ingredients("Barbeque Sauce",0.2,1500,"Ingredients1")
# add_ingredients("Mayo",0.2,1500,"Ingredients1")
# add_ingredients("Hot Sauce",0.2,1500,"Ingredients1")
# add_ingredients("Pineapple Slices",0.6,800,"Ingredients1")

# add_ingredients("Salad",2.5,1000,"ingredients")
# add_ingredients("Coca Cola Can",1.1,1500,"ingredients")
# add_ingredients("Fanta Can",1.1,1500,"ingredients")
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
