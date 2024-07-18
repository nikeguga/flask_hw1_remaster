from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        'title': 'Home'
    }
    return render_template('base.html', **context)

@app.route('/clothing')
def clothing():
    clothing_items = ['T-shirt', 'Jeans', 'Jacket']
    context = {
        'title': 'Clothing',
        'items': clothing_items
    }
    return render_template('clothing.html', **context)

@app.route('/shoes')
def shoes():
    shoes_items = ['Sneakers', 'Boots', 'Sandals']
    context = {
        'title': 'Shoes',
        'items': shoes_items
    }
    return render_template('shoes.html', **context)

@app.route('/jacket')
def jacket():
    jacket_items = ['Black Jacket', 'Blue Jacket', 'Red Jacket']
    context = {
        'title': 'Jacket',
        'items': jacket_items
    }
    return render_template('jacket.html', **context)

if __name__ == '__main__':
    app.run(debug=True)
