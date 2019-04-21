from flask import Flask, render_template, url_for, request,redirect
from werkzeug.datastructures import ImmutableMultiDict

from inventory import get_inventory
from side import sides
from drink import drinks
from order import Order
from system import OrderSystem
from main import *

app = Flask(__name__)
app.secret_key = "ed1f3de267e251db"

side1 = sides()
drink1 = drinks()
meal1 = meals()
order1 = Order()
sys = OrderSystem()


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
    return render_template('main.html')

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

@app.route("/order/purchased/")
def purchased():
    return render_template('Purchased_Order.html')



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

@app.route("/order/",methods = ['POST','GET'])
def make_order():
    global order1
    sys.make_booking(order1)
    order1 = Order()
    side1._sides = []
    drink1._drinks = []
    meal1._burgers = []
    meal1._wraps = []
    return redirect(url_for('purchased'))

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
