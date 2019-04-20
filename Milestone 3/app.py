#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from src.inventory import Inventory

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy
'''
Home Page
'''
@app.route("/")
def home():
    return render_template('sides.html')




'''
Ordering Sides
'''
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
Ordering Drinks
'''
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
Checkout
'''
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    order = Order(ordered_main, ordered_sides, ordered_drinks)

    return render_template('checkout.html', order=order)



if __name__ == '__main__':
    app.run(debug=True)
