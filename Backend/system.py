from mains3 import Sauce
from mains3 import Ingredients
from mains3 import Food

#Create others
def addSauce(sauce1):
    Sauce.ingredient.append(sauce1)

#Testing adding new items functions
sauce = Food('mayo',0,0.4)
sauce1 = Food('chilli',0,0.3)
addSauce(sauce)
#Sauce.printSauce()
addSauce(sauce1)
Sauce.printSauce()


#For make order function, should take in same parameters as order1
#Checks if the ingredients are available
#if it is then make order (using the order class)
#Have another class honestly, will make things so much easier
#the class will consist of time_ordered (use datetime),id,status,and obv the order itself
#when you make an order, append it to an order list
