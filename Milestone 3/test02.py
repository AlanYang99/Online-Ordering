from drink import drinks
from main import meals, wraps, burgers, burgerIngredients, wrapIngredients, Ingredients
from side import sides
from system import Orders, OrderID, increment_ingredients, increment_burger_ingredients, increment_wraps_ingredients, increment_sides, increment_drinks
from inventory import get_inventory
import pickle
import pytest

@pytest.fixture
def sys():
    return Orders()

class TestOrderID():
    def test_order_id(self, sys):
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
        
        order_id = OrderID(my_order)

        assert order_id._id == 1