import sqlite3
#from sqlite3.dbapi2 import Cursor

try:
    conn = sqlite3.connect('Provision_Store.db')
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS Provision_Store(
                        product_id INTEGER PRIMARY KEY,
                        Product_name TEXT NOT NULL,
                        Price REAL NOT NULL,
                        Manufacturing_date TEXT,
                        Quantity INTEGER
            )"""
    cursor.execute(query)
    conn.commit()
    print("Table successfully created")
except conn.Error as error:
    print("Error creating table", error)


Inventory_List = [(1, "Kalyppo", 1.50, "21-05-21", 45),
                  (2, "Bread", 5.50, "22-03-21", 68),
                  (3, "Rice", 200, "25-04-21", 100),
                  (4, "Voltic", 1.70, "20-01-21", 35),
                  (5, "Fanta", 2.50, "25-02-21", 70),
                  (6, "Oreos", 3.80, "16-04-21", 20),
                  (7, "Coke", 2.80, "30-04-21", 300),
                  (8, "Popcorn", 3.00, "22-03-21", 40),
                  (9, "Sugar", 5.00, "05-05-21", 18),
                  (10, "CornFlakes", 21.00, "15-05-21", 30)]

def insert_inventorylists(lists):
    try:
        conn = sqlite3.connect("Provision_Store")
        cursor = conn.cursor()
        # product_id = list[0]
        # Product_name = list[1]
        # Price = list[2]
        # Manufacturing_date = list[3]
        # Quantity = list[4]
        query = """INSERT INTO Provision_Store ( product_id, Product_name, Price, Manufacturing_date, Quantity)
                                    VALUES (?, ?, ?, ?, ?, ? )"""
        print("Insert successful!", lists)
        cursor.executemany(query, lists)#(product_id, Product_name, Price, Manufacturing_date, Quantity))
        conn.commit()
        print("Insert successful")
    except conn.Error as error:
        print('Error inserting into Table', error)
    finally:
        if conn:
            conn.close()

insert_inventorylists(Inventory_List)