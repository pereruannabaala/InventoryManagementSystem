from flask import Flask, render_template

import psycopg2

app = Flask(__name__)

conn=psycopg2.connect("host='localhost' user='postgres' password='1234' dbname='dukalangu'")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    cur=conn.cursor()
    q="SELECT * FROM products;"
    cur.execute(q)
    r=cur.fetchall()
    print(r)
    return render_template('products.html',rows=r)
    
    

@app.route('/sales')
def sales():
    cur=conn.cursor()
    p="SELECT * FROM sales;"
    cur.execute(p)
    s=cur.fetchall()
    print(s)
    return render_template('sales.html', sales=s)




if __name__ == "__main__":
    app.run()
 