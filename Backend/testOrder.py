from sides import food
from sides import sides
from order import Order
from drinks import drinks



foods1 = food('coke',2,2)
drinks1 = drinks(foods1)
foods2 = food('nuggest',1,2)
sides1 = sides(foods2)

order1 = Order(sides1,drinks1)
order1.printTotal()

#print(order1._sides)

errors = {
    food('meat',2,2) : 2
}
