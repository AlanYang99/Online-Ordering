from drink import drinks
from main import meals, burgers, burgerIngredients, Ingredients
from side import sides
from system import Orders, increment_ingredients, increment_burger_ingredients, increment_wraps_ingredients, increment_sides, increment_drinks
from inventory import get_inventory
import pickle
import pytest

@pytest.fixture
def sys():
    return Orders()

class TestOrderMeals():
    def test_successful_order_burger_sides_drink(self, sys):
        mains = meals()

        ingredients = Ingredients()
        ingredients.set_ingredients("Cheddar Cheese",1)
        ingredients.set_ingredients("Tomato Slices",3)
        ingredients.set_ingredients("Bacon",1)

        burger_ingredients = burgerIngredients()
        burger_ingredients.set_burgerIngredients("Sesame Seed Bun",2)
        burger_ingredients.set_burgerIngredients("Wagyu Beef",1)

        burger = burgers(ingredients, burgerIngredients)
        mains.addBurger(burger)

        order_side = sides()
        order_side.set_sides("Fries",1)

        order_drink = drinks() 
        order_drink.set_drinks("Fanta Bottle",1)

        my_order = sys.make_order(mains,order_side,order_drink)

        assert order_side.get_sides     == "    1x Fries : $1<br>"
        assert order_side.price         == 1
        assert order_drink.get_drinks   == "    1x Fanta Bottle : $2<br>"
        assert order_drink.price        == 2
        #assert mains.getIngredients     == ''  #todo
        #assert my_order.totalCost       == 3   #todo
        #assert my_order.printTotal()    == ""  #todo

    def test_successful_order_sides(self,sys):
        order_side = sides()
        order_side.set_sides("Fries",1)

        mains = None
        drinks = None

        my_order = sys.make_order(mains,order_side,drinks)

        assert order_side.get_sides     == "    1x Fries : $1<br>"
        assert order_side.price         == 1
        assert my_order.totalCost       == 1 
        assert my_order.printTotal()    == "    1x Fries : $1<br>"

    def test_successful_order_drinks(self,sys):
        order_drink = drinks() 
        order_drink.set_drinks("Fanta Bottle",1)

        mains = None
        sides = None

        my_order = sys.make_order(mains,sides,order_drink)

        assert order_drink.get_drinks   == "    1x Fanta Bottle : $2<br>"
        assert order_drink.price        == 2
        assert my_order.totalCost       == 2 
        assert my_order.printTotal()    == "    1x Fanta Bottle : $2<br>"

    def test_order_nothing(self,sys):
        mains = None
        sides = None
        drinks = None

        my_order = sys.make_order(mains,sides,drinks)

        assert my_order.totalCost       == 0 
        assert my_order.printTotal()    == "No Orders Currently Made"


class TestIncrementIngredients():
    def test_successful_increment_ingredients(self,sys):
        name   = "Bacon"
        amount = 1

        inventory = get_inventory("Ingredients")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_ingredients(name,amount)

        inventory = get_inventory("Ingredients")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after - amount_before == amount

    def test_unsuccessful_increment_ingredients(self,sys):
        name          = "Pickles"
        amount        = 1
        amount_before = None
        amount_after  = None

        inventory = get_inventory("Ingredients")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_ingredients(name,amount)

        inventory = get_inventory("Ingredients")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after  == None
        assert amount_before == None

    def test_successful_increment_burger_ingredients(self,sys):
        name   = "English Muffin"
        amount = 1

        inventory = get_inventory("burgerIngredients")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_burger_ingredients(name,amount)

        inventory = get_inventory("burgerIngredients")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after - amount_before == amount

    def test_unsuccessful_increment_burger_ingredients(self,sys):
        name          = "Pickles"
        amount        = 1
        amount_before = None
        amount_after  = None

        inventory = get_inventory("burgerIngredients")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_burger_ingredients(name,amount)

        inventory = get_inventory("burgerIngredients")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after  == None
        assert amount_before == None

    def test_successful_increment_wrap_ingredients(self,sys):
        name = "Pita"
        amount = 1

        inventory = get_inventory("wrapIngredients")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_wraps_ingredients(name,amount)

        inventory = get_inventory("wrapIngredients")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after - amount_before == amount

    def test_unsuccessful_increment_wrap_ingredients(self,sys):
        name          = "Pickles"
        amount        = 1
        amount_before = None
        amount_after  = None

        inventory = get_inventory("wrapIngredients")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_wraps_ingredients(name,amount)

        inventory = get_inventory("wrapIngredients")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after  == None
        assert amount_before == None
    
    def test_successful_increment_sides(self,sys):
        name = "Fries"
        amount = 1

        inventory = get_inventory("sides")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_sides(name,amount)

        inventory = get_inventory("sides")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after - amount_before == amount

    def test_unsuccessful_increment_sides(self,sys):
        name          = "Pickles"
        amount        = 1
        amount_before = None
        amount_after  = None

        inventory = get_inventory("sides")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_sides(name,amount)

        inventory = get_inventory("sides")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after  == None
        assert amount_before == None
    
    def test_successful_increment_drinks(self,sys):
        name = "Fanta Bottle"
        amount = 1

        inventory = get_inventory("drinks")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_drinks(name,amount)

        inventory = get_inventory("drinks")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after - amount_before == amount

    def test_unsuccessful_increment_drinks(self,sys):
        name          = "Pickles"
        amount        = 1
        amount_before = None
        amount_after  = None

        inventory = get_inventory("drinks")
        for i in inventory:
            if i._name == name:
                amount_before = i._amount
        
        increment_wraps_ingredients(name,amount)

        inventory = get_inventory("drinks")
        for i in inventory:
            if i._name == name:
                amount_after = i._amount
        
        assert amount_after  == None
        assert amount_before == None