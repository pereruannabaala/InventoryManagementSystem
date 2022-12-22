from flask import Flask, render_template,request,redirect

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
    # print(r)
    return render_template('products.html', rows=r)
    
    

@app.route('/sales')
def sales():
    cur=conn.cursor()
    p="SELECT * FROM sales;"
    cur.execute(p)
    s=cur.fetchall()
    # print(s)
    v="select * from products"
    cur.execute(v)
    w=cur.fetchall()
    return render_template('sales.html',sales=s,products=w)

@app.route('/add_products',methods=['POST'])
def add_products():
    cur=conn.cursor()
    n=request.form["name"]
    b=request.form["bprice"]
    z=request.form["sprice"]
    q=request.form["squantity"]
    data=(n,b,z,q)
    a="insert into products(name,buying_price,selling_price,stock_quantity) values(%s,%s,%s,%s);"
    cur.execute(a,data)
    conn.commit()
    return redirect('/products')
@app.route('/add_sales',methods=['POST'])
def add_sales():
    cur=conn.cursor()
    pid=request.form["pid"]
    qua=request.form["quantity"]
    sales=(pid,qua,'now()')
    h="insert into sales(quantity,pid,created_at) values(%s,%s,%s);"
    cur.execute(h,sales)
    conn.commit()
    return redirect('/sales')

if __name__ == "__main__":
    app.run()
 