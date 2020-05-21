from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
	connection = mysql.connector.connect(
		user = 'root',
        password = 'root',
        database = 'Inventory')

	cursor = connection.cursor()
	cursor.execute("SELECT * from `Inventory`.`tbl_product_movement`;")
	return str(cursor.column_names)

if __name__ == '__main__':
    app.run()

    