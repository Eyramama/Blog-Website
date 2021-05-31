import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def delete_task(conn, quantity):
    sql = 'DELETE FROM ProvisionStore WHERE quantity =?'
    cur = conn.cursor()
    cur.execute(sql, (quantity,))
    conn.commit()


try:
    conn = sqlite3.connect('Provision_store4.db')
    cursor = conn.cursor()
    query = """CREATE TABLE IF NOT EXISTS ProvisionStore (
                       product_id INTEGER PRIMARY KEY,
                       name TEXT NOT NULL,
                       price REAL NOT NULL,
                       manufacturing_date TEXT,
                       quantity INTEGER
        )"""
    cursor.execute(query)
    conn.commit()
    print("Table successfully created")
except conn.Error as error:
    print("Error creating Table", error)


InventoryLists = [(1,"Kalypo",1.50, "21-05-2021", 45),
                 (2,"Bread", 5.50, "22-03-2021", 68),
                 (3,"Rice",200, "25-04-2021", 100),
                 (4,"Yam", 15.50, "28-12-2021", 43),
                 (5,"Popcorn", 10.50, "14-12-2021", 36),
                 (6,"Oreos", 7.50, "11-11-2021",53),
                 (7,"Voltic", 4.50, "1-12-2021", 109),
                 (8,"Apples", 2.50, "2-12-2021", 107),
                 (9,"Fanta", 1.50, "12-12-2021", 5)]

def insert_inventorylists(list):
    try:
        conn = sqlite3.connect('Provision_store4.db')
        cursor = conn.cursor()

        query = """INSERT INTO ProvisionStore (product_id, name, price, manufacturing_date, quantity)              
                                                VALUES (?,?,?,?,?)"""
        print("Insert successful!", InventoryLists)
        cursor.executemany(query,InventoryLists)
        #conn.execute("DELETE from Provision_ store where ID = 2;")
        conn.commit()
        print("Insert successful")
    except conn.Error as error:
        print("Error inserting into Table", error)
    finally:
            if conn:
                conn.close()


def main():
    insert_inventorylists(InventoryLists)
    database = r"C:\Users\intern.TURNTABL\VSC\Provision_store4.db"
    conn = create_connection(database)
    with conn:
        delete_task(conn, 45)

if __name__ == '__main__':
    main()
