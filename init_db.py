import sqlite3
from datetime import datetime, timezone

connection = sqlite3.connect('inventory.db')


with open('schema.sql') as f:
	connection.executescript(f.read())

cur = connection.cursor()


# Create 4 Products
cur.execute("INSERT INTO product (product_id) VALUES (?)",
            (1,)
            )
cur.execute("INSERT INTO product (product_id) VALUES (?)",
            (2,)
            )
cur.execute("INSERT INTO product (product_id) VALUES (?)",
            (3,)
            )
cur.execute("INSERT INTO product (product_id) VALUES (?)",
            (4,)
            )

# Create 4 Locations
cur.execute("INSERT INTO location (location_id) VALUES (?)",
            (1,)
            )
cur.execute("INSERT INTO location (location_id) VALUES (?)",
            (2,)
            )
cur.execute("INSERT INTO location (location_id) VALUES (?)",
            (3,)
            )
cur.execute("INSERT INTO location (location_id) VALUES (?)",
            (4,)
            )


# Make 20 ProductMovements


# 1. Move Product 1 to Location 1 (100 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (1, datetime.now(timezone.utc), None, 1, 1, 100)
           )

# 2. Move Product 2 to Location 2 (100 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (2, datetime.now(timezone.utc), None, 2, 2, 100)
           )

# 3. Move Product 3 to Location 3 (100 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (3, datetime.now(timezone.utc), None, 3, 3, 100)
           )

# 4. Move Product 4 to Location 4 (100 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (4, datetime.now(timezone.utc), None, 4, 4, 100)
           )

# 5. Move Product 1 from Location 1 to Location 2 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (5, datetime.now(timezone.utc), 1, 2, 1, 20)
           )

# 6. Move Product 1 from location 2 to location 3 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (6, datetime.now(timezone.utc), 2, 3, 1, 20)
           )

# 7. Move Product 1 from Location 3 to Location 4 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (7, datetime.now(timezone.utc), 3, 4, 1, 20)
           )

# 8. Move Product 1 from Location 4 to Location 1 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (8, datetime.now(timezone.utc), 4, 1, 1, 20)
           )

#==============20 units of Product 1 have completed 1 rotation=========

# 9. Move Product 2 from Location 2 to Location 3 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (9, datetime.now(timezone.utc), 2, 3, 2, 20)
           )

# 10. Move Product 2 from Location 3 to Location 4 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (10, datetime.now(timezone.utc), 3, 4, 2, 20)
           )

# 11. Move Product 2 from Location 4 to Location 1 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (11, datetime.now(timezone.utc), 4, 1, 2, 20)
           )

# 12. Move Product 2 from Location 1 to Location 2 (20 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (12, datetime.now(timezone.utc), 1, 2, 2, 20)
           )

#==============20 units of Product 2 have completed 1 rotation=========

# 13. Move Product 3 from Location 3 to Location 4 (30 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (13, datetime.now(timezone.utc), 3, 4, 1, 30)
           )

# 14. Move Product 3 from Location 3 to Location 2 (30 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (14, datetime.now(timezone.utc), 3, 4, 1, 30)
           )

# 15. Move Product 3 from Location 3 to Location 1 (40 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (15, datetime.now(timezone.utc), 3, 1, 3, 40)
           )

#==============Now Product 3 is finished at Location 3=========

# 16. Move Product 4 from Location 4 to Location 3 (30 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (16, datetime.now(timezone.utc), 4, 3, 4, 30)
           )

# 17.  Move Product 4 from Location 4 to Location 2 (30 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (17, datetime.now(timezone.utc), 4, 2, 4, 30)
           )

# 18.  Move Product 4 from Location 4 to Location 1 (40 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (18, datetime.now(timezone.utc), 4, 1, 4, 40)
           )

#==============Now Product 4 is finished at Location 3=========

# 19.  Move Product 4 from Location 2 to Location 1 (10 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (19, datetime.now(timezone.utc), 2, 1, 4, 10)
           )

# 20.  Move Product 3 from Location 1 to Location 2 (10 units)

cur.execute("INSERT INTO product_movement (movement_id, movement_date, from_location, to_location, product_id, quantity) VALUES (?, ?, ?, ?, ?, ?)",
            (20, datetime.now(timezone.utc), 1, 2, 3, 10)
           )



connection.commit()
connection.close()

    