from inventory import Food
from Utility import haveItem
import pickle

class sides():

    def __init__(self):
        self._sides = []

    def set_sides(self,side,amount): #Holy shit this function
                                    #CAn help me automatically decrement items
        found = 0
        infile = open("sides", "rb")
        sides = pickle.load(infile)
        infile.close()
        # if(haveItem(self._sides,side)):
        #     for i in self._sides:
        #         if(side == i._name):
        #             i._amount += amount
        # else:
        #     self._sides.append(Food(side, i._price, amount))

        #Code subject to change when we introduce large fries, etc
        if(haveItem(self._sides,side)):
            for i in self._sides:
                if (side == i._name):
                    i._amount += amount
                    break
        else:
            for i in sides:
                if(i._name == side):
                    self._sides.append(Food(side,i._price,amount))
                    break
        # for i in sides:
        #     if(i._name == side):
        #         if(haveItem(self._sides,side)):
        #             for i in self._sides:
        #                 if(i._name == side):
        #                     i._amount += amount
        #         else:
        #             self._sides.append(Food(side, i._price, amount))
        #             break

        #self._sides.append(Food(side._name,side._price,side))

    @property
    def get_sides(self):
        sides_list = ' '
        for side in self._sides:
            sides_list += "   " + str(side)
        return sides_list

    @property
    def price(self):
        cost = 0
        for side in self._sides:
            cost+= (side._amount * side._price)
        return cost
