from flask import Flask, render_template, url_for, request,redirect
from werkzeug.datastructures import ImmutableMultiDict

from inventory import get_inventory
from side import sides
from drink import drinks
from order import Order

app = Flask(__name__)

side1 = sides()
drink1 = drinks()


@app.route("/")
def home():
    return render_template('home.html')






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



if __name__ == '__main__':
    app.run(debug=True)
