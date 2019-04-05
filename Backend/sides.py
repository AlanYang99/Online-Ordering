
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
