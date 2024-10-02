import sqlite3

# Connect to SQLite
connection = sqlite3.connect("ecommerce_inventory.db")

# Create a cursor object to insert records and create table
cursor = connection.cursor()

# Create the table for eCommerce store inventory if it doesn't exist
table_info = """
CREATE TABLE IF NOT EXISTS INVENTORY (
    PRODUCT_NAME VARCHAR(50),
    CATEGORY VARCHAR(50),
    IN_STOCK BOOLEAN,
    PRICE REAL
);
"""
cursor.execute(table_info)

# Sample product data (100 products with various categories, stock status, and prices)
products = [
    ('Laptop', 'Electronics', 1, 1200.99),
    ('Headphones', 'Electronics', 0, 89.99),
    ('Coffee Mug', 'Home and Kitchen', 1, 12.50),
    ('T-Shirt', 'Clothing', 1, 25.00),
    ('Desk Chair', 'Furniture', 0, 199.99),
    ('Smartphone', 'Electronics', 1, 699.99),
    ('Blender', 'Home and Kitchen', 1, 49.99),
    ('Sneakers', 'Clothing', 1, 60.00),
    ('Bookshelf', 'Furniture', 1, 150.99),
    ('Air Conditioner', 'Electronics', 0, 499.99),
    ('Washing Machine', 'Home Appliances', 1, 399.99),
    ('Smartwatch', 'Electronics', 1, 149.99),
    ('Jeans', 'Clothing', 1, 40.00),
    ('Sofa', 'Furniture', 1, 799.99),
    ('Electric Kettle', 'Home and Kitchen', 1, 29.99),
    ('Gaming Mouse', 'Electronics', 1, 45.00),
    ('Office Desk', 'Furniture', 0, 350.00),
    ('Tennis Racket', 'Sports', 1, 70.00),
    ('Basketball', 'Sports', 1, 30.00),
    ('Fridge', 'Home Appliances', 1, 899.99),
    ('Microwave Oven', 'Home Appliances', 1, 150.00),
    ('LED TV', 'Electronics', 1, 999.99),
    ('Bluetooth Speaker', 'Electronics', 1, 75.00),
    ('Shampoo', 'Personal Care', 1, 10.99),
    ('Conditioner', 'Personal Care', 1, 9.99),
    ('Tablet', 'Electronics', 1, 299.99),
    ('Monitor', 'Electronics', 1, 250.00),
    ('Running Shoes', 'Clothing', 1, 85.00),
    ('Winter Jacket', 'Clothing', 1, 120.00),
    ('Cookware Set', 'Home and Kitchen', 1, 99.99),
    ('Yoga Mat', 'Sports', 1, 25.00),
    ('Bike Helmet', 'Sports', 1, 45.00),
    ('Rice Cooker', 'Home Appliances', 1, 60.00),
    ('Electric Toothbrush', 'Personal Care', 1, 29.99),
    ('Face Cream', 'Personal Care', 1, 19.99),
    ('Lawn Mower', 'Garden', 0, 199.99),
    ('BBQ Grill', 'Garden', 1, 150.00),
    ('Garden Shears', 'Garden', 1, 25.99),
    ('Vacuum Cleaner', 'Home Appliances', 1, 129.99),
    ('Dishwasher', 'Home Appliances', 0, 750.00),
    ('Electric Drill', 'Tools', 1, 89.99),
    ('Hammer', 'Tools', 1, 19.99),
    ('Nail Gun', 'Tools', 0, 150.00),
    ('Power Bank', 'Electronics', 1, 29.99),
    ('Wireless Charger', 'Electronics', 1, 19.99),
    ('Keyboard', 'Electronics', 1, 40.00),
    ('Mouse Pad', 'Electronics', 1, 10.00),
    ('Router', 'Electronics', 1, 59.99),
    ('Modem', 'Electronics', 0, 80.00),
    ('Graphics Card', 'Electronics', 1, 500.00),
    ('External Hard Drive', 'Electronics', 1, 120.00),
    ('Hair Dryer', 'Personal Care', 1, 35.00),
    ('Shaving Kit', 'Personal Care', 1, 25.00),
    ('Perfume', 'Personal Care', 1, 50.00),
    ('Body Lotion', 'Personal Care', 1, 15.99),
    ('Water Bottle', 'Home and Kitchen', 1, 12.99),
    ('Backpack', 'Clothing', 1, 45.00),
    ('Sunglasses', 'Clothing', 1, 60.00),
    ('Formal Shoes', 'Clothing', 1, 90.00),
    ('Leather Belt', 'Clothing', 1, 30.00),
    ('Handbag', 'Clothing', 1, 80.00),
    ('Curtains', 'Home Decor', 1, 50.00),
    ('Wall Clock', 'Home Decor', 1, 25.00),
    ('Lamp', 'Home Decor', 1, 40.00),
    ('Carpet', 'Home Decor', 0, 100.00),
    ('Bed Sheets', 'Home and Kitchen', 1, 35.00),
    ('Towels', 'Home and Kitchen', 1, 25.00),
    ('Iron', 'Home Appliances', 1, 40.00),
    ('Juicer', 'Home Appliances', 1, 75.00),
    ('Toaster', 'Home Appliances', 1, 25.00),
    ('Blow Dryer', 'Personal Care', 1, 30.00),
    ('Lipstick', 'Personal Care', 1, 10.00),
    ('Earrings', 'Clothing', 1, 15.00),
    ('Necklace', 'Clothing', 1, 50.00),
    ('Watch', 'Clothing', 1, 200.00),
    ('Fitness Tracker', 'Electronics', 1, 150.00),
    ('Action Camera', 'Electronics', 1, 350.00),
    ('Camping Tent', 'Sports', 1, 150.00),
    ('Sleeping Bag', 'Sports', 1, 60.00),
    ('Fishing Rod', 'Sports', 1, 100.00),
    ('Treadmill', 'Sports', 0, 800.00),
    ('Dumbbells', 'Sports', 1, 70.00),
    ('Protein Powder', 'Sports', 1, 40.00),
    ('Bicycle', 'Sports', 1, 400.00),
    ('Helmet', 'Sports', 1, 45.00),
    ('Jacket', 'Clothing', 1, 100.00),
    ('Dress', 'Clothing', 1, 80.00),
    ('Socks', 'Clothing', 1, 15.00),
    ('Suit', 'Clothing', 1, 250.00),
    ('Hoodie', 'Clothing', 1, 60.00),
    ('Pants', 'Clothing', 1, 50.00)
]

# Insert product records into the INVENTORY table
cursor.executemany("INSERT INTO INVENTORY VALUES (?, ?, ?, ?)", products)

# Display all records in the INVENTORY table
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM INVENTORY''')
for row in data:
    print(row)

# Commit your changes to the database
connection.commit()

# Close the connection
connection.close()
