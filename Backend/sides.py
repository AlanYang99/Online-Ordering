
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


class item:

    def __init__(price,amount): #not sure if we need name
        self.price = price
        self.amount = amount

class big:

    def __init__(self):
        self.fries = [small_fries == item(0.5,1),medium_fries == item(1,1),large_fries == item(2,1)]
        self.nuggets =

    def printprice(self):
        price = 0
        for i in self.fries:
            price += i.price
        return fries

    def setFries(self,amount,size):
        for i in self.fries:
            i.amount = amount
        #OR

    def setsmallFriest(self,amount):
        self.fries[0].amount = amount
