#!/usr/bin/env python3
from flask import Flask, render_template, url_for, request,redirect
from werkzeug.datastructures import ImmutableMultiDict

from inventory import get_inventory
from side import sides
from drink import drinks
from order import Order

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

side1 = sides()
drink1 = drinks()

'''
Home Page
'''
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

'''
Ordering Sides

from src.side import Sides
@app.route("/sides", methods=["GET", "POST"])
def order_sides():
    ordered_sides = Sides()
    available_sides = ['Chips', 'Nuggs'] #Inventory.get_sides()
    print(available_sides)

    if request.method == "POST":
        for item in available_sides:
            num_side = request.form.get(item)
            if num_side is not '' and num_side is not '0':
                print(item,num_side)
                #ordered_sides.set_sides(item,num_side)

    return render_template('sides.html',sides=available_sides)
'''

@app.route("/drinks/")
def drink():
    return render_template('drink.html',drink_list = get_inventory("drinks"))

'''
Ordering Drinks
from src.drink import Drinks
@app.route("/drinks", methods=["GET", "POST"])
def order_drinks():
    ordered_drinks = Drinks()
    available_drinks = Inventory.get_drinks()

    if request.method == "POST":
        for item in available_drinks:
            num_drink = request.form.get(item)
            if num_drink is not '' and num_drink is not '0':
                ordered_drinks.set_drinks(item,num_drink)

    return render_template('sides.html',drinks=available_drinks)
'''

@app.route("/order/")
def order():
    return render_template('order.html')

@app.route("/track/")
def track():
    return render_template('track.html')


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
    if(side1._sides == []):
        return "No Side Purchases"
    return Order(None,side1,drink1).printTotal

@app.route("/drinks/", methods = ['POST','GET'])
def getDrinks():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        global drink1
        for state, capital in quantity_list.items():
            if(not(capital.isdigit()) or int(capital) == 0):
                continue
            print(int(capital))
            drink1.set_drinks(state,int(capital))

        # print(type(order1))
        #quantity_list = f.getlist('quantity')
        #So quantity_list is now  a list of values corresponding to the users
        #Ordered quantities of items.
        #In sides, for special products like fries (which comes in varying) sizes
        #do a if statement, if get_inventory , item is = fries, and decrement for large, medium small subsequently

    global order1

    if(drink1._drinks == []):
        return "<h1>You made no Side Orders</h1>"
    return Order(None,side1,drink1).printTotal

@app.route("/create-your-own/burger/", methods = ['POST','GET'])
def make_burger():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        print(quantity_list)
    return "Hello"

@app.route("/create-your-own/wrap/", methods = ['POST','GET'])
def make_wrap():
    if request.method == 'POST':
        quantity_list = request.form.to_dict()
        print(quantity_list)
    return "Hello"

if __name__ == '__main__':
    app.run(debug=True)

'''
Questions to ask Ian
2. About the ingredients, for example sundae is made up of chocolate topping and
   ice-cream, is it possible if I decrement an inventory object called Chocolate Sundae
   or do  i need to decrement the ingredients used to make a sundae (ice-cream, topping)
   Or is it pure up to my choice
3. About the folders issue
'''
