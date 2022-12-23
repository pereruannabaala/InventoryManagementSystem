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
    t="select sales.sid,products.name,sales.quantity,(sales.created_at) from products join sales on products.id=sales.pid;"
    cur.execute(t)
    x=cur.fetchall()
    # print(x)

    v="select * from products;"
    cur.execute(v)
    w=cur.fetchall()
    return render_template('sales.html',sales=x,products=w,new=s)


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
    

@app.route('/dashboard')
def dashboard():
    cur=conn.cursor()
    dash="select sum(p.selling_price * s.quantity) as Sales, p.name from products as p join sales as s on p.id=s.pid group by p.name;"
    cur.execute(dash)
    k=cur.fetchall()
    print(k)
    labels=[]
    data=[]
    colors=[]
    for i in k:
        labels.append(i[1].split("-")[-1])
        data.append(i[0])
        colors.append("#8e5ea2")
    return render_template('dashboard.html',label=labels,data=data,colors=colors)





if __name__ == "__main__":
    app.run()
 