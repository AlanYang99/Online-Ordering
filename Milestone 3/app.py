<<<<<<< HEAD
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

if __name__ == '__main__':
    app.run(debug=True)
