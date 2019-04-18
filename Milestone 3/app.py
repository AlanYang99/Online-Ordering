from flask import Flask, render_template
from src.side import Sides, side1
from src.system import orders

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('layout.html')

@app.route("/sides", methods=["POST"])
def order_sides():
    sides = Sides()

    if request.method == "POST":
        for item in sides.get_sides(): # not a list, its a string so im not sure about this
            num_side = request.form.get(item)
            if side is not '':
                sides.set_sides(item,num_side)

    return render_template('sides.html',sides=sides.get_sides())

if __name__ == '__main__':
    app.run(debug=True)
