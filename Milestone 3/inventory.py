import pickle
class Food:
    '''
    Utility class for ingredients or food in general, which has the
    attributes: name, price, amount
    '''
    def __init__(self,name,price,amount):
        self._name = name
        self._price = price
        self._amount = amount

    # def __str__(self):
    #     return f"{self._amount}x {self._name} : ${round(self._amount * self._price,2)}<br>"
    #     # output = f"{self._amount}x {self._name} : ${self._amount * self._price}\n"

    def __repr__(self):
        return f'{self._name},{self._price},{self._amount}'



def get_inventory(inventory_type):
    infile = open(inventory_type,'rb')
    inventory = pickle.load(infile)
    infile.close()
    return inventory
# print(get_inventory("Ingredients"))
print(get_inventory("Ingredients1"))
