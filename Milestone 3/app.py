from flask import Flask, render_template, url_for, request,redirect
from werkzeug.datastructures import ImmutableMultiDict

from inventory import get_inventory
from side import sides
from drink import drinks
from order import Order
from system import OrderSystem
from system import sys
from system import increment_ingredients, increment_ingredients1
from system import increment_wraps_ingredients, increment_burger_ingredients
from system import increment_sides, increment_drinks,decrement_stock
from main import *

app = Flask(__name__)
app.secret_key = "ed1f3de267e251db"

side1 = sides()
drink1 = drinks()
meal1 = meals()
order1 = Order()
id1 = 0



@app.route("/")
def home():
    return render_template('home.html')

@app.route("/create-your-own/")
def new_main():
    return render_template('creation.html')

@app.route("/create-your-own/burger/")
def new_burger():
    return render_template('burger.html',ingredient_list = get_inventory('ingredients'),
                            ingredient_list2 = get_inventory('ingredients1'),
                            ingredient_list3 = get_inventory('burgerIngredients'))

@app.route("/create-your-own/wrap/")
def new_wrap():
    return render_template('wrap.html',ingredient_list = get_inventory('ingredients'),
                            ingredient_list2 = get_inventory('ingredients1'),
                            ingredient_list3 = get_inventory('wrapIngredients'))

@app.route("/mains/")
def main():
    global meal1
    return render_template('main.html',burger = meal1._Luger_Burger
                                ,wrap = meal1._Luger_Wrap)

@app.route("/mains/",methods = ['POST','GET'])
def add_mains():
    if request.method == 'POST':
        burger_amount = request.form['burger']
        wrap_amount = request.form['wrap']
        global meal1
        global order1
        if(burger_amount.isdigit() and int(burger_amount) != 0):
            meal1.add_Luger_Burger(int(burger_amount))
        if(wrap_amount.isdigit() and int(wrap_amount) != 0):
            meal1.add_Luger_Wrap(int(wrap_amount))

        order1.set_mains(meal1)
        return redirect(url_for('order'))


@app.route("/sides/")
def side():
    return render_template('side.html',side_list = get_inventory("sides"))

@app.route("/drinks/")
def drink():
    return render_template('drink.html',drink_list = get_inventory("drinks"))

@app.route("/order/")
def order():
    return render_template('order.html',order = order1)

@app.route("/track/")
def track():
    return render_template('track.html')



@app.route("/staff/main-inventory/")
def main_inventory():
    return render_template('main_inventory.html',inventory1 = get_inventory("Ingredients"),
                                                inventory2 = get_inventory("Ingredients1"))

@app.route("/staff/burger-inventory/")
def burger_inventory():
    return render_template('burger_inventory.html',inventory = get_inventory("burgerIngredients"))

@app.route("/staff/wrap-inventory/")
def wrap_inventory():
    return render_template('wrap_inventory.html',inventory = get_inventory("wrapIngredients"))

@app.route("/staff/side-inventory/")
def side_inventory():
    return render_template('side_inventory.html',inventory = get_inventory("sides"))

@app.route("/staff/drink-inventory/")
def drink_inventory():
    return render_template('drink_inventory.html',inventory = get_inventory("drinks"))

@app.route("/track/")
def track_order():
    return render_template('track.html')

@app.route("/track/<id>")
def id_track(id):
    order = sys.get_order(id)
    if(order == None):
         return redirect(url_for('page_not_found'))
    else:
        return render_template('Order_details1.html',order = order)

@app.route("/track/",methods = ['POST','GET'])
def get_id():
    if request.method == 'POST':
        id = request.form['id']
        # print(id)
        order = sys.get_order(id)

        if(order == None):
            return redirect(url_for('page_not_found'))
        else:
            return redirect(url_for('id_track',id = id))
# @app.route("/order/burger-inventory/")
# def purchased():
#     return render_template('Purchased_Order.html')
#
# @app.route("/order/wrap-inventory/")
# def purchased():
#     return render_template('Purchased_Order.html')



#Thanks to lab08
@app.route('/404/')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

#Thanks to lab08
@app.route("/staff/")
def staff():
    return render_template('staff.html',order_list = sys._orders)

#Thanks to lab08
@app.route("/staff/<id>/")
def access_orders(id):

    order = sys.get_order(id)

    if (order == None):
        return redirect(url_for('page_not_found'))

    return render_template('Order_details.html',order = order)

@app.route("/staff/<id>/",methods = ['POST','GET'])
def update_orders(id):
    if "update" in request.form:
        sys.update_status(id)
        return redirect(url_for('access_orders',id = id))
    elif "delete" in request.form:
        sys.delete_order(id)
        return redirect(url_for('staff'))

#when making the order ensure self._sides, self._drinks are all reseted
@app.route("/sides/", methods = ['POST','GET'])
def getSides():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        global side1
        for state, capital in quantity_list.items():
            if(not(capital.isdigit()) or int(capital) == 0):
                continue
            side1.set_sides(state,int(capital))

        # print(type(order1))
        #quantity_list = f.getlist('quantity')
        #So quantity_list is now  a list of values corresponding to the users
        #Ordered quantities of items.
        #In sides, for special products like fries (which comes in varying) sizes
        #do a if statement, if get_inventory , item is = fries, and decrement for large, medium small subsequently

    global order1
    order1.set_sides(side1)
    if(side1._sides == []):
        return "No Side Purchases"
    return redirect(url_for('order'))

@app.route("/drinks/", methods = ['POST','GET'])
def getDrinks():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        global drink1
        for state, capital in quantity_list.items():
            if(not(capital.isdigit()) or int(capital) == 0):
                continue
            drink1.set_drinks(state,int(capital))

        # print(type(order1))
        #quantity_list = f.getlist('quantity')
        #So quantity_list is now  a list of values corresponding to the users
        #Ordered quantities of items.
        #In sides, for special products like fries (which comes in varying) sizes
        #do a if statement, if get_inventory , item is = fries, and decrement for large, medium small subsequently

    global order1
    order1.set_drinks(drink1)
    if(drink1._drinks == []):
        return "<h1>You made no Side Orders</h1>"
    return redirect(url_for('order'))

@app.route("/create-your-own/burger/", methods = ['POST','GET'])
def make_burger():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        burg1 = burgerIngredients()
        ingr1 = Ingredients()
        i = 0
        for state, capital in quantity_list.items():
            i+=1
            if(not(capital.isdigit()) or int(capital) == 0):
                continue
            if(i >= 6):
                ingr1.set_ingredients(state,int(capital))
            else:
                burg1.set_burgerIngredients(state,int(capital))
        #print(ingr1.getIngredients)
        #print(burg1.get_burgerIngredients)
        global meal1
        meal1.addBurger(burgers(ingr1,burg1,quantity_list['quantity']))
        global order1
        order1.set_mains(meal1)
    #    print(burge1.getIngredients)
    return redirect(url_for('order'))

@app.route("/create-your-own/wrap/", methods = ['POST','GET'])
def make_wrap():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        wrap1 = wrapIngredients()
        ingr1 = Ingredients()
        i = 0
        for state, capital in quantity_list.items():
            i+=1
            if(not(capital.isdigit()) or int(capital) == 0):
                continue
            if(i >= 6):
                ingr1.set_ingredients(state,int(capital))
            else:
                wrap1.set_wrapIngredients(state,int(capital))
        #print(ingr1.getIngredients)
        #print(burg1.get_burgerIngredients)
        global meal1
        meal1.addWrap(wraps(ingr1,wrap1,quantity_list['quantity']))
        global order1
        order1.set_mains(meal1)
    #    print(burge1.getIngredients)
    return redirect(url_for('order'))

@app.route("/order/purchased/")
def purchased():
    global id1
    return render_template('Purchased_Order.html',id = id1)

@app.route("/order/",methods = ['POST','GET'])
def make_order():
    global id1
    global side1
    global order1
    global drink1
    global meal1

    order = sys.make_booking(order1)

    #decreasing burgers
    for burger in meal1._burgers:
        for ingredient in burger._ingredients._ingredients:
            name = ingredient._name
            amount = int(ingredient._amount) * int(burger._amount)
            decrement_stock("Ingredients", name, amount)
            decrement_stock("Ingredients1", name, amount)
        for ingredient in burger._burgerIngredients._burgerIngredients:
            name = ingredient._name
            amount = int(ingredient._amount) * int(burger._amount)
            decrement_stock("burgerIngredients", name, amount)

    #decreasing wraps
    for wrap in meal1._wraps:
        for ingredient in wrap._ingredients._ingredients:
            name = ingredient._name
            amount = int(ingredient._amount) * int(wrap._amount)
            decrement_stock("Ingredients", name, amount)
            decrement_stock("Ingredients1", name, amount)
        for ingredient in wrap._wrapIngredients._wrapIngredients:
            name = ingredient._name
            amount = int(ingredient._amount) * int(wrap._amount)
            decrement_stock("wrapIngredients", name, amount)

    #decreasing sides
    for side in side1._sides:
        name = side._name
        amount = side._amount
        decrement_stock("sides", name, amount)

    #decreasing drinks
    for drink in drink1._drinks:
        name = drink._name
        amount = drink._amount
        decrement_stock("drinks", name, amount)

    id1 = order._id
    order1 = Order()
    order1._sides = None
    order1._drinks = None
    order1._mains = None
    side1 = sides()
    drink1 = drinks()
    meal1 = meals()
    side1._sides = []
    drink1._drinks = []
    meal1._burgers = []
    meal1._wraps = []
    return redirect(url_for('purchased'))

@app.route("/staff/main-inventory/",methods = ['POST','GET'])
def increment_main_inventory():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        i = 0
        for state, capital in quantity_list.items():
            i+=1
            if(not(capital.isdigit())):
                continue
            if(i >= 8):
                increment_ingredients1(state,int(capital))
            else:
                increment_ingredients(state,int(capital))

    return redirect(url_for('main_inventory'))

@app.route("/staff/burger-inventory/",methods = ['POST','GET'])
def increment_burger_inventory():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        i = 0
        for state, capital in quantity_list.items():
            if(not(capital.isdigit())):
                continue
            if(int(capital) != 0):
                i = 1
            increment_burger_ingredients(state,int(capital))

        return redirect(url_for('burger_inventory'))



@app.route("/staff/wrap-inventory/",methods = ['POST','GET'])
def increment_wrap_inventory():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        print(quantity_list)
        for state, capital in quantity_list.items():
            if(not(capital.isdigit())):
                continue
            increment_wraps_ingredients(state,int(capital))

    return redirect(url_for('wrap_inventory'))

@app.route("/staff/side-inventory/",methods = ['POST','GET'])
def increment_side_inventory():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        for state, capital in quantity_list.items():
            if(not(capital.isdigit())):
                continue
            increment_sides(state,int(capital))

    return redirect(url_for('side_inventory'))

@app.route("/staff/drink-inventory/",methods = ['POST','GET'])
def increment_drink_inventory():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        for state, capital in quantity_list.items():
            if(not(capital.isdigit())):
                continue
            increment_drinks(state,int(capital))


    return redirect(url_for('drink_inventory'))





if __name__ == '__main__':
    app.run(debug=True)

'''
Questions to ask Ian
1. Doing the project (Iteration3) solo
2. About the ingredients, for example sundae is made up of chocolate topping and
   ice-cream, is it possible if I decrement an inventory object called Chocolate Sundae
   or do  i need to decrement the ingredients used to make a sundae (ice-cream, topping)
   Or is it pure up to my choice
3. About the folders issue
'''
