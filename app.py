from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__, 
	template_folder='/Users/srpatil/Desktop/Suraj/DevOps/Projects/flask-test/templates',
	static_folder='/Users/srpatil/Desktop/Suraj/DevOps/Projects/flask-test/static')

connection = mysql.connector.connect(
	user = 'root',
	password = 'root',
    database = 'Inventory')

cursor = connection.cursor()

@app.route('/')
@app.route('/home')
def home():
	cursor.execute("SELECT * from `Inventory`.`tbl_product_movement`;")
	data = cursor.fetchall() #data from database
	return render_template("template.html", my_string="Product Movement Table", value=data)

@app.route('/products')
def products():
	cursor.execute("SELECT * from `Inventory`.`tbl_product`;")
	data = cursor.fetchall() #data from database
	return render_template("template.html", my_string="Product Table", value=data)

@app.route('/locations')
def locations():
	cursor.execute("SELECT * from `Inventory`.`tbl_location`;")
	data = cursor.fetchall() #data from database
	return render_template("template.html", my_string="Location Table", value=data)

@app.route('/js/<path:path>')
def send_js(path): 
	return send_from_directory('js', path)

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

if __name__ == '__main__':
    app.run()

    