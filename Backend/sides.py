
class food:

    def __init__(self,name,price,amount):
        self.name = name
        self.price = price
        self.amount = amount

class sides:

    def __init__(self,small_fries ,med_fries = None, large_fries =None,six_nuggets = None,ten_nuggets = None):
        self.small_fries = small_fries
        self.med_fries = med_fries
        self.large_fries = large_fries
        self.six_nuggets = six_nuggets
        self.ten_nuggets = ten_nuggets

    def sidesprice(self):
        return self.small_fries.price * self.small_fries.amount #gonna finalise this later

    def printSides(self):
        return f'small_fries {self.small_fries.amount}'


class big:

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
        if(found is 0)
            print("Side not found")

    def printprice(self):
        price = 0
        for i in self.fries:
            price += i.price
        for i in self.nuggets
            price+=i.price
        for i in self.others
            price += i.price
        return price

    def getSides(self):
        sides = ''
        for i in self.fries:
            sides += f'{i.name} : {i.amount}'
        for i in self.nuggets:
            sides += f'{i.name} : {i.amount}'
        for i in self.others:
            sides += f'{i.name} : {i.amount}'
        return sides

        
