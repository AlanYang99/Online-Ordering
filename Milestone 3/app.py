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




if __name__ == '__main__':
    app.run(debug=True)
