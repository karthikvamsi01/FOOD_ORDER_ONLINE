from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample menu items (you can load this from a database)
menu = [
    {"name": "Burger", "price": 5.99},
    {"name": "Pizza", "price": 7.99},
    {"name": "Salad", "price": 3.99},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def view_menu():
    return render_template('menu.html', menu=menu)

@app.route('/order', methods=['POST'])
def place_order():
    item_name = request.form.get('item_name')
    item_price = request.form.get('item_price')
    return render_template('order.html', item_name=item_name, item_price=item_price)

if __name__ == '__main__':
    app.run(debug=True)