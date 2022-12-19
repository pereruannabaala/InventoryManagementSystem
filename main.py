from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')




if __name__ == "__main__":
    app.run()
 