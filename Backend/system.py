from mains3 import Sauce
from mains3 import Ingredients
from mains3 import Food
import datetime

class order_id:

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

class orders:

    def __init__(self):
        self._orders = []

    def deleteOrder(self,id):
        for order in self._orders:
            if order._id is order:
                self._orders.remove(order)

    def getOrder(self,id):
        for order in self._orders:
            if order._id is order:
                return order
        return None

    def make_order(self,mains,sides,drinks):

        #Checking if available ingredients 1st
        new_order = Order(mains,sides,drinks)
        self._orders.append(new_order)









#Create others
def addSauce(sauce):
    Sauce.ingredient.append(sauce1)

def addVegetables(vege):
    Vegetables.ingredient.append(vege)

"""
#Testing adding new items functions
sauce = Food('mayo',0,0.4)
sauce1 = Food('chilli',0,0.3)
addSauce(sauce)
#Sauce.printSauce()
addSauce(sauce1)
Sauce.printSauce()
"""



#For make order function, should take in same parameters as order1
#Checks if the ingredients are available
#if it is then make order (using the order class)
#Have another class honestly, will make things so much easier
#the class will consist of time_ordered (use datetime),id,status,and obv the order itself
#when you make an order, append it to an order list
