from flask import Flask, render_template, request
import os
import sqlite3

os.system("python init_db.py") #Script to set up the Database and execute product movements

home_dir = os.getcwd()

app = Flask(__name__, 
	template_folder= home_dir + '/templates',
	static_folder= home_dir + '/static')

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
@app.route('/home')
def home():
	conn = get_db_connection()
	data = conn.execute('SELECT * FROM product_movement').fetchall()
	conn.close()
	return render_template("template.html", my_string="Product Movement ID", value=data)

@app.route('/products')
def products():
	conn = get_db_connection()
	data = conn.execute('SELECT * FROM product').fetchall()
	conn.close()
	return render_template("template.html", my_string="Product ID", value=data)

@app.route('/locations')
def locations():
	conn = get_db_connection()
	data = conn.execute('SELECT * FROM location').fetchall()
	conn.close()
	return render_template("template.html", my_string="Location ID", value=data)

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)

    