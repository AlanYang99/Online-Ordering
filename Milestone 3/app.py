#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy
'''
Home Page
'''
@app.route("/")
def home():
    return render_template('sides.html')




'''
Ordering Mains
'''
@app.route("/mains")
def order_mains():
    return render_template('sides.html')



'''
Ordering Sides
'''
from src.side import Sides
from src.inventory import Inventory
@app.route("/sides", methods=["GET", "POST"])
def order_sides():
    ordered_sides = Sides()
    inventory = Inventory()
    available_sides = inventory.get_sides()
    print(available_sides)

    if request.method == "POST":
        for item in available_sides: 
            num_side = request.form.get(item)
            if num_side is not '':
                ordered_sides.set_sides(item,num_side)
        print(ordered_sides.get_sides)

    return render_template('sides.html',sides=available_sides)



'''
Ordering Drinks
'''
@app.route("/")
def order_drinks():
    return render_template('sides.html')




if __name__ == '__main__':
    app.run(debug=True)
