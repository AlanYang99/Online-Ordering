class Food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

class Sides:

    def __init__(self):
        self.fries = [Food('smallfries',2,0),Food('mediumfries',3,0),Food('largefries',4,0)]
        self.nuggets =[Food('sixnuggets',6,0),Food('tennuggets',10,0)]
        self.others = [Food('sundae',2,0)]

    def set_small_Fries(self,amount):
        self.fries[0].amount = amount

    def set_medium_fries(self,amount):
        self.fries[1].amount = amount

    def set_large_fries(self,amount):
        self.fries[2].amount = amount

    def set_six_nuggets(self,amount):
        self.nuggets[0].amount = amount

    def set_ten_nuggets(self,amount):
        self.nuggets[1].amount = amount

    def set_other_sides(self,side,amount):
        found = 0
        for i in self.others:
            if(i.name is side):
                found = 1
                i.amount = amount
        if(found is 0):
            print("Side not found")

    def printprice(self):
        price = 0
        for i in self.fries:
            price += i.price * i.amount
        for i in self.nuggets:
            price += i.price * i.amount
        for i in self.others:
            price += i.price * i.amount
        return price

    def getSides(self):
        sides = ''
        for i in self.fries:
            sides += f'{i.name} : {i.amount}\n'
        for i in self.nuggets:
            sides += f'{i.name} : {i.amount}\n'
        for i in self.others:
            sides += f'{i.name} : {i.amount}\n'
        return sides

side1 = sides()
side1.set_small_Fries(3)
side1.set_medium_fries(1)
side1.set_six_nuggets(4)
side1.set_other_sides('sundae',4)
"""
print(side1.getSides())
print(side1.printprice())
"""
