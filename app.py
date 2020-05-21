from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, template_folder='/Users/srpatil/Desktop/Suraj/DevOps/Projects/flask-test')

connection = mysql.connector.connect(
	user = 'root',
	password = 'root',
    database = 'Inventory')

cursor = connection.cursor()

@app.route('/')
def index():
	cursor.execute("SELECT * from `Inventory`.`tbl_product_movement`;")
	data = cursor.fetchall() #data from database
	return render_template("index.html", value=data)

@app.route('/products')
def products():
	cursor.execute("SELECT * from `Inventory`.`tbl_product`;")
	data = cursor.fetchall() #data from database
	return render_template("products.html", value=data)


@app.route('/locations')
def locations():
	cursor.execute("SELECT * from `Inventory`.`tbl_location`;")
	data = cursor.fetchall() #data from database
	return render_template("locations.html", value=data)

if __name__ == '__main__':
    app.run()

    