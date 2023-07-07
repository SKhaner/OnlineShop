import sqlite3
from flask import Flask, session, render_template, redirect, url_for, request, url_for

app = Flask('app')
app.secret_key = "secret"


@app.route('/', methods=['GET', 'POST'])
def index():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM product WHERE category = 'Dive'")
    # Diveproducts = cursor.fetchall()
    # cursor.execute("SELECT * FROM product WHERE category = 'Dress'")
    # Dressproducts = cursor.fetchall()
    # cursor.execute("SELECT * FROM product WHERE category = 'Grail'")
    # Grailproducts = cursor.fetchall()
    cursor.execute("SELECT * FROM product ORDER BY category")
    products = cursor.fetchall()
    if request.method == 'POST':
      # print(request.form["filter"])
      cursor.execute("SELECT * FROM product WHERE category=?", (request.form["filter"], ))
      products = cursor.fetchall()
      return render_template("index.html", p = products, f=(request.form["filter"]+' Watches'))
    return render_template("index.html", p = products, f='All Products')


@app.route('/prodpage/<prod>')
def prodpage(prod):
  connection = sqlite3.connect("myDatabase.db")
  connection.row_factory = sqlite3.Row
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM product WHERE name = ?", (prod, ))
  x = cursor.fetchone()
  return render_template("prodpage.html", name=x)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        session['s'] = request.form["searched"]
        # #print("hello1")#for debugging
        # #print(session['s'])#for debugging
        return redirect(url_for('results'))
    return render_template("search.html")


@app.route('/results')
def results():
    # #print("hello1")#gets here
    searched = session.get('s', None)
    # #print(searched)#gets here
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM product WHERE name LIKE ? OR category LIKE ?", (
            '%' + searched + '%',
            '%' + searched + '%',
        ))
    s = cursor.fetchall()
    return render_template("results.html", s=s)


@app.route('/login', methods=['GET', 'POST'])
def login():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    if request.method == 'POST':
        user = request.form["user_name"]
        passw = request.form["user_pass"]
        cursor.execute(
            "SELECT * FROM customer WHERE username = ? AND password = ?",
            (user, passw))
        rows = cursor.fetchone()
        if rows:
            session['username'] = user
            session['password'] = passw
            session['cart'] = []
            return redirect('/loggedin')
        else:
            return redirect('/login_fail')

    return render_template("login.html")


@app.route('/login_fail', methods=['GET', 'POST'])
def login_fail():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customer")
    if request.method == 'POST':
        user = request.form["user_name"]
        passw = request.form["user_pass"]
        cursor.execute(
            "SELECT * FROM customer WHERE username = ? AND password = ?",
            (user, passw))
        rows = cursor.fetchone()
        if rows:
            session['username'] = user
            session['password'] = passw
            return redirect('/loggedin')
        else:
            return redirect('/login_fail')

    return render_template("login_fail.html")


@app.route('/loggedin', methods=['GET', 'POST'])
def loggedin():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    # cursor.execute("SELECT * FROM product WHERE category = 'Dive'")
    # Diveproducts = cursor.fetchall()
    # cursor.execute("SELECT * FROM product WHERE category = 'Dress'")
    # Dressproducts = cursor.fetchall()
    # cursor.execute("SELECT * FROM product WHERE category = 'Grail'")
    # Grailproducts = cursor.fetchall()
    cursor.execute("SELECT * FROM product ORDER BY category")
    products = cursor.fetchall()
    if request.method == 'POST':
      # print(request.form["filter"])
      cursor.execute("SELECT * FROM product WHERE category=?",(request.form["filter"], ))
      products = cursor.fetchall()
      return render_template("loggedin.html", p = products, f=(request.form["filter"]+' Watches'))
    return render_template("loggedin.html", p = products, f='All Products')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # Log the current user out and redirect them to the login page
    #session.pop(session['username'], None)
    #session.pop(session['password'], None)
    #session.pop(session['cart'], None)
    session.clear()
    return redirect('/')


@app.route('/add_cart/<product_id>',
           methods=['GET', 'POST'])  #ADDING PRODUCTS TO CART
def add_cart(product_id):
    if 'here' not in session:
      session['here'] = True
    # #print("t1")
      connection = sqlite3.connect("myDatabase.db")
      connection.row_factory = sqlite3.Row
      cursor = connection.cursor()
      connection.commit()
      cursor.execute("SELECT * FROM product WHERE name = ?", (product_id, ))
      prod = cursor.fetchone()
      cart = []
      session['quanity'] = 1
  
      #if the user entered a quantity make that the session var, if not session var = 1
      if request.method == 'POST':
          if not request.form["quanity"] == "":
              session['quanity'] = request.form["quanity"]
  
      #if cart is empty
      if 'cart' not in session or session['cart'] is None:
          # #print("in if")
          cart.append([
              str(prod[0]), session['quanity'],
              int(prod[2]) * int(session['quanity'])
          ])  #add quantity here
          session['cart'] = cart
          session.pop('here', None)
          # #print(session['quanity'])
      #if cart has at least 1 item in it
      else:
          #If item already exists in cart
          # #print("in else")
          cart = session['cart']
          # #print(cart)
          # #print("1")
          #if item is already in cart update quanity
          x = any(str(prod[0]) in sublist for sublist in cart)
          if x == True:
              for x in cart:
                  if x[0] == str(prod[0]):
                      x[1] = str(int(session['quanity']) + int(x[1]))
                      x[2] = int(x[1]) * int(prod[2])
                      session['cart'] = cart
                      session.pop('quanity', None)
                      session.pop('here', None)
                      return render_template("cart.html")
  
          #is item is not in cart, add to cart
          cart.append([
              str(prod[0]), session['quanity'],
              int(prod[2]) * int(session['quanity'])
          ])
          #cart.append(str(prod[0]))
          # #print(cart)
          # #print("2")
          #cart = session['cart']
          #cart = cart + (";" + str(prod[0])) # should have a request form that takes in however much a user wants from a certain product
          session['cart'] = cart
          session.pop('here', None)
          # #print(session['quanity'])
          # #print(session['cart'])
      # #print(cart)
      # #print("3")
      return render_template("cart.html")

    else:
      # print("redirected")
      session.pop('here', None)
      return redirect(url_for('view_cart'))


@app.route('/view_cart')
def view_cart():
    return render_template("cart.html")


@app.route('/clear_cart')
def clear_cart():
    #session['cart'] = []
    session.pop('cart', None)
    return render_template("cart.html")


@app.route('/checkout')
def checkout():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if not session['cart']:
      return redirect(url_for('loggedin'))
    else:
      cart = session['cart']
    #go through session['cart'] execute a query to update stock where name=NameError
    for x in cart:
        n = x[0]
        q = x[1]
        cursor.execute("SELECT * FROM product WHERE name = ?", (n, ))
        l = cursor.fetchone()
        # #print("fetched")
        if int(q) > l['stock']:
            # #print("over")
            return render_template("over.html")
        if int(q) == 0:
          cart.pop(cart.index(x))
          if not session['cart']:
            return redirect(url_for('loggedin'))
          # return redirect(url_for('loggedin'))
          
        cursor.execute("UPDATE product SET stock = stock-? WHERE name=?", (
            q,
            n,
        ))
    connection.commit()
    total = 0
    for x in session['cart']:
        total += int(x[2])
    # print(total)  #gets to this point
    #get order number
    cursor.execute("SELECT COUNT(*) FROM customerOrder WHERE id = ?",
                   (session['username'], ))
    c = cursor.fetchone()
    # print(c[0])
    #add order to customerOrders with incremented order number
    cursor.execute("SELECT date()")
    date = cursor.fetchone()
    # print(date[0])
    cursor.execute(
        "INSERT INTO customerOrder (id, orderNumber, cost, pdate) VALUES (?,?,?,?)",
        (session['username'], int(int(c[0]) + 1), total, date[0]))
    connection.commit()
    cart = session['cart']
    #add cart to a seperate table
    for x in cart:
        # print("in for")
        # print(c[0])
        cursor.execute(
            "INSERT INTO itemsOrdered (id, orderNumber, items, quantity, cost) VALUES (?,?,?,?,?)",
            (session['username'], str(c[0] + 1), str(x[0]), str(x[1]), int(x[2])))
        # print("commit")
        connection.commit()
    # print("added to prev")
    session.pop('cart', None)

    return render_template("checkedout.html")


@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    connection.commit()
    cursor.execute("SELECT * FROM product WHERE name = ?", (name, ))
    prod = cursor.fetchone()
    if request.method == 'POST':
        # print("in if")
        cart = session['cart']
        x = any(name in sublist for sublist in cart)
        if x == True:
            for x in cart:
                if x[0] == name:
                    # # print("found name")
                    if request.form["new"] != "":
                      x[1] = request.form["new"]
                    elif request.form["new"] == "":
                      x[1] = x[1]
                    # # print(x[1])
                    # # print(prod[2])
                    x[2] = int(x[1]) * int(prod[2])
                    session['cart'] = cart
                    # # print("quanity updated")
                    return render_template("cart.html")


@app.route('/signup', methods=['GET', 'POST'])
def signuup():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    if request.method == 'POST':
        # #print("post")#for debugging
        name = request.form["name"]
        userid = request.form["user_name"]
        password = request.form["user_pass"]
        cursor.execute("SELECT * FROM customer WHERE username = ?", (userid, ))
        get = cursor.fetchone()
        if get is None:
          cursor.execute(
              "INSERT INTO customer (username, password, name) VALUES (?,?,?)",
              (userid, password, name))
          connection.commit()
          # #print("execute succes")#for debugging
          #cursor.execute("SELECT * FROM customer WHERE username = ?", (userid, ))#for debugging
          #x = cursor.fetchall()#for debugging
          # #print(x)#for debugging
          session['username'] = userid
          session['password'] = password
          return redirect('/loggedin')
        else:
          return render_template("signup.html", x = 1)

    return render_template("signup.html")


@app.route('/prev_orders', methods=['GET', 'POST'])
def prev_orders():
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customerOrder WHERE id=?",
                   (session['username'], ))
    history = cursor.fetchall()
    cursor.execute("SELECT * FROM itemsOrdered WHERE id=?", (session['username'],))
    items = cursor.fetchall()

    if request.method == 'POST':
      order = request.form["sort"]
      if order == 'incDate':
        connection = sqlite3.connect("myDatabase.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customerOrder WHERE id=? ORDER BY pdate",
                       (session['username'], ))
        history = cursor.fetchall()
        cursor.execute("SELECT * FROM itemsOrdered WHERE id=?", (session['username'],))
        items = cursor.fetchall()
        return render_template("prev_orders.html", history=history, items = items)
      if order == 'decDate':
        connection = sqlite3.connect("myDatabase.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customerOrder WHERE id=? ORDER BY pdate DESC",
                       (session['username'], ))
        history = cursor.fetchall()
        cursor.execute("SELECT * FROM itemsOrdered WHERE id=?", (session['username'],))
        items = cursor.fetchall()
        return render_template("prev_orders.html", history=history, items = items)
        
    return render_template("prev_orders.html", history=history, items = items)


@app.route('/searchPrevOrder', methods=['GET', 'POST'])
def searchPrevOrder():
    if request.method == 'POST':
        session['s'] = request.form["searched"]
        # #print("hello1")#for debugging
        # #print(session['s'])#for debugging
        return redirect(url_for('resultsPrevOrder'))
    return render_template("searchPrevOrder.html")


@app.route('/resultsPrevOrder')
def resultsPrevOrder():
    # #print("hello1")#gets here
    searched = session.get('s', None)
    # #print(searched)#gets here
    connection = sqlite3.connect("myDatabase.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM customerOrder WHERE id=? AND orderNumber LIKE ? OR pdate LIKE ?",
                       (session['username'], searched, searched))
    history = cursor.fetchall()
    cursor.execute("SELECT * FROM itemsOrdered WHERE id=?", (session['username'],))
    items = cursor.fetchall()
    return render_template("resultsPrevOrder.html", history=history, items = items)

@app.route('/delete/<prod>', methods=['GET', 'POST'])
def delete(prod):

  if request.method == 'POST':
    cart = session['cart']
    i = 0
    for x in cart:
      if str(x[0]) == str(prod):
        cart.pop(i)
      else:
        i+=1

    session['cart'] = cart
    
  return redirect(url_for('view_cart'))


app.run(host='0.0.0.0', port=8080)
