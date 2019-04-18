from inventory import Food
import pickle

class Sides():

    def __init__(self):
        self._sides = []

    def set_sides(self,side,amount):
        found = 0
        infile = open("sides", "rb")
        sides = pickle.load(infile)
        infile.close()
        for i in sides:
            if(i._name == side):
                self._sides.append(Food(i._name, i._price, amount))
                found = 1
                break
        if(found == 0):
            print("Side is not found")

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
