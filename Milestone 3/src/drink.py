from inventory1 import Food
import pickle

class drinks():

    def __init__(self):
        self._drinks = []

    def set_drinks(self,drink,amount):
        found = 0
        infile = open("drinks", "rb")
        drinks = pickle.load(infile)
        infile.close()
        for i in drinks:
            if(i._name == drink):
                self._drinks.append(Food(i._name, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Drink is not found")

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
