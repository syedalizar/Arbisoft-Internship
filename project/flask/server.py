from flask import Flask, render_template, request, redirect, session
from flaskext.mysql import MySQL
from socket import gethostname
app = Flask(__name__)


mysql = MySQL()

#configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'MUrchamp20ns!'
app.config['MYSQL_DATABASE_DB'] = 'orsaydb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

conn = mysql.connect() #connection variable

cursor = conn.cursor()

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST': #accepts post request from the home route
        return redirect('/products')

    result = cursor.execute("SELECT DISTINCT category FROM product_table;")
    #fetching all categories from database
    if result > 0:
        categories = cursor.fetchall()
        return render_template('home.html', categories=categories)
        #rendering home.html and sending the list of unique categories to it

@app.route('/products/<category>') #passing the selected category as a parameter
def products(category): #receiving the selected category
    # print("category: ")
    # print(category)


    # print(category.split("'")[1])

    query_template= "SELECT * FROM product_table WHERE category = {}"
    result = cursor.execute(query_template.format("'" + category.split("'")[1]) + "'")
    #query for selection of all products of the category

    if result > 0:
        products = cursor.fetchall()
        return render_template('products.html', products = products)

# app run configurations
if __name__ == '__main__':
    app.run(debug=True)
