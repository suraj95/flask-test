# Flask-Test

![alt text](./images/inventory.png)

For more details, refer to this [Page](https://frappe.io/flask-test)

This repository contains the code I wrote for the Flask-test by Frappe.io. The goal is to create a web application using Flask framework to manage inventory of a list of products in respective warehouses. Imagine this application will be used in a shop or a warehouse that needs to keep track of various products and various locations. 

# Inventory Management Web Application

The goal is to create a web application using Flask framework to manage inventory of a list of products in respective warehouses. Imaging this application will be used in a shop or a warehouse that needs to keep track of various products and various locations

The application should covers the following functionalities:

## Database Tables:

- Product (product_id)
- Location (location_id)
- ProductMovement (movement_id, timestamp, from_location, to_location, product_id, qty)

Note: Any one, or both of from_location and to_location can be filled. If we want to move things into a location, from_location will be blank, if we want to move things out, then to_location will be blank.

## Views:

- Add/Edit/View Product
- Add/Edit/View Location
- Add/Edit/View ProductMovement

## Report:
- Balance quantity in each location

## Use Cases:
- Create 3/4 Products
- Create 3/4 Locations
- Make 20 ProductMovements
- Get product balance in each Location in a grid view, with 3 columns: Product, Warehouse, Qty




