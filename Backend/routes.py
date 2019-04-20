from flask import render_template, request, redirect, url_for, abort
from server import app
from datetime import datetime
from inventory1 import Food
import pickle

#loading in pickles
infile = open("burgerIngredients", "rb")
inventory = pickle.load(infile)
infile.close()

posts = []

for i in inventory:
    posts.append(Food(i._name, i._price, i._amount))

# posts = [
#     {
#         'test': '1',
#         'name': 'brioche',
#         'price': '$1',
#         'amount': '100',
#     },
#     {
#         'test': '2',
#         'name': 'sesame',
#         'price': '$1.50',
#         'amount': '50',
#     }
# ]

@app.route("/")
#@app.route("/inventory")
def inventory():
    return render_template('inventory.html', posts=posts)

# '''
# Dedicated page for "page not found"
# '''
# @app.route('/404')
# def page_not_found(e=None):
#     return render_template('404.html'), 404

