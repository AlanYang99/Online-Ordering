from inventory import Food
from Utility import have_item
import pickle

class Drinks():

    def __init__(self):
        self._drinks = []

    def set_drinks(self,drink,amount):
        infile = open("drinks", "rb")
        drinks = pickle.load(infile)
        infile.close()
        if(have_item(self._drinks,drink)):
            for i in self._drinks:
                if (drink == i._name):
                    i._amount += amount
                    break
        else:
            for i in drinks:
                if(i._name == drink):
                    self._drinks.append(Food(drink, i._price, amount))
                    break


    @property
    def get_drinks(self):
        drink_list = ' '
        for drink in self._drinks:
            drink_list += "   " + str(drink)
        return drink_list

    @property
    def price(self):
        cost = 0
        for drink in self._drinks:
            cost+= (drink._amount * drink._price)
        return cost
