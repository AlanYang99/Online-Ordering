from drink import drinks
from main import meals, wraps, burgers, burgerIngredients, wrapIngredients, Ingredients
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
        order_mains = meals()

        ingredients = Ingredients()
        ingredients.set_ingredients("Cheddar Cheese",1)
        ingredients.set_ingredients("Tomato Slices",3)
        ingredients.set_ingredients("Bacon",1)

        burger_ingredients = burgerIngredients()
        burger_ingredients.set_burgerIngredients("Sesame Seed Bun",2)
        burger_ingredients.set_burgerIngredients("Wagyu Beef",1)

        burger = burgers(ingredients, burger_ingredients)
        order_mains.addBurger(burger)

        order_side = sides()
        order_side.set_sides("Fries",1)

        order_drink = drinks() 
        order_drink.set_drinks("Fanta Bottle",1)

        my_order = sys.make_order(order_mains,order_side,order_drink)

        assert my_order.totalCost       == 13.6
        assert my_order.printTotal      == "Plain burger:\n     1x Cheddar Cheese : $0.5<br>   3x Tomato Slices : $1.5<br>   1x Bacon : $0.6<br>    2x Sesame Seed Bun : $4<br>   1x Wagyu Beef : $4<br>    1x Fanta Bottle : $2<br>    1x Fries : $1<br>"

    def test_successful_order_wrap_sides_drink(self, sys):
        order_mains = meals()

        ingredients = Ingredients()
        ingredients.set_ingredients("Grilled Chicken",2)
        ingredients.set_ingredients("Tomato Slices",3)
        ingredients.set_ingredients("Fried Egg",1)

        wrap_ingredients = wrapIngredients()
        wrap_ingredients.set_wrapIngredients("Pita",1)

        wrap = wraps(ingredients, wrap_ingredients)
        order_mains.addWrap(wrap)

        order_side = sides()
        order_side.set_sides("Fries",1)

        order_drink = drinks() 
        order_drink.set_drinks("Strawberry Milkshake",1)

        my_order = sys.make_order(order_mains,order_side,order_drink)

        assert my_order.totalCost       == 15.8
        assert my_order.printTotal      == "Plain wrap:\n     2x Grilled Chicken : $7.0<br>   3x Tomato Slices : $1.5<br>   1x Fried Egg : $0.8<br>    1x Pita : $3<br>    1x Strawberry Milkshake : $2.5<br>    1x Fries : $1<br>"

    def test_successful_order_wrap(self, sys):
        order_mains = meals()

        ingredients = Ingredients()
        ingredients.set_ingredients("Grilled Chicken",2)
        ingredients.set_ingredients("Tomato Slices",3)
        ingredients.set_ingredients("Fried Egg",1)

        wrap_ingredients = wrapIngredients()
        wrap_ingredients.set_wrapIngredients("Pita",1)

        wrap = wraps(ingredients, wrap_ingredients)
        order_mains.addWrap(wrap)

        order_side = None

        order_drink = None

        my_order = sys.make_order(order_mains,order_side,order_drink)

        assert my_order.totalCost       == 12.3
        assert my_order.printTotal      == "Plain wrap:\n     2x Grilled Chicken : $7.0<br>   3x Tomato Slices : $1.5<br>   1x Fried Egg : $0.8<br>    1x Pita : $3<br>"

    def test_successful_order_burger_sides_drink(self, sys):
        order_mains = meals()

        ingredients = Ingredients()
        ingredients.set_ingredients("Cheddar Cheese",1)
        ingredients.set_ingredients("Tomato Slices",3)
        ingredients.set_ingredients("Bacon",1)

        burger_ingredients = burgerIngredients()
        burger_ingredients.set_burgerIngredients("Sesame Seed Bun",2)
        burger_ingredients.set_burgerIngredients("Wagyu Beef",1)

        burger = burgers(ingredients, burger_ingredients)
        order_mains.addBurger(burger)

        order_side = None
        order_drink = None

        my_order = sys.make_order(order_mains,order_side,order_drink)

        assert my_order.totalCost       == 10.6
        assert my_order.printTotal      == "Plain burger:\n     1x Cheddar Cheese : $0.5<br>   3x Tomato Slices : $1.5<br>   1x Bacon : $0.6<br>    2x Sesame Seed Bun : $4<br>   1x Wagyu Beef : $4<br>"
 
    def test_successful_order_sides(self,sys):
        order_side = sides()
        order_side.set_sides("Fries",1)

        mains = None
        drinks = None

        my_order = sys.make_order(mains,order_side,drinks)

        assert my_order.totalCost       == 1 
        assert my_order.printTotal      == "    1x Fries : $1<br>"

    def test_successful_order_drinks(self,sys):
        order_drink = drinks() 
        order_drink.set_drinks("Fanta Bottle",1)

        mains = None
        sides = None

        my_order = sys.make_order(mains,sides,order_drink)

        assert my_order.totalCost       == 2 
        assert my_order.printTotal      == "    1x Fanta Bottle : $2<br>"

    def test_order_nothing(self,sys):
        mains = None
        sides = None
        drinks = None

        my_order = sys.make_order(mains,sides,drinks)

        assert my_order.totalCost       == 0 
        assert my_order.printTotal      == "No Orders Currently Made"


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
        name          = "Durian"
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
        name          = "Durian"
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
        name          = "Durian"
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
        name          = "Durian"
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
        name          = "Durian"
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