import sqlite3
from sqlite3.dbapi2 import Cursor

# try:  
#     conn = sqlite3.connect('internship_demo.db')
#     cursor = conn.cursor()
#     #query = """SELECT sqlite_version()"""
#     query = """INSERT INTO interns ( intern_id, first_name, last_name, email, phone_number, school  )
#                            VALUES (1, "Chantelle", "Osafo", "cosafo@gmail.com", "0123456", "Ashesi" )"""
#     cursor.execute(query)
#     print("Insert successful!")
#     #result = cursor.fetchall()
#     #print('Database successfully opened. Version is , ', result)
#     #print('Table successfully created.')
# except conn.Error as error:
#     print('Error inserting into Table', error)
# finally:
#     if conn:
#         conn.close()

interns_list = [(2, "Enoch", "Sem", "enochsem@gmail.com", "0555444433", "UCC"),
                (3, "Vanessa", "Bedzra", "vanessabedzra@gmail.com", "02415181954", "Ashesi"),
                (4,"George", "Arthur", "georgearthur@gmail.com", "0241578805", "Ashesi"),
                (5, "Hilda", "Ajara", "hilda@gmail.com", "0544432689", "UCC")]

def insert_interns(list):
    try:  
        conn = sqlite3.connect('internship_demo.db')
        cursor = conn.cursor()
        # intern_id = list[0]
        # first_name = list[1]
        # last_name = list[2]
        # email = list[3]
        # phone_number = list[4]
        # school = list[5]
        #query = """SELECT sqlite_version()"""
        query = """INSERT INTO interns ( intern_id, first_name, last_name, email, phone_number, school)
                            VALUES (?, ?, ?, ?, ?, ? )"""
        #cursor.execute(query)
        print("Insert successful!", list)
        cursor.execute(query, list) #(intern_id, first_name, last_name, email, phone_number, school)
        conn.commit()
        print("Insert successful")
        #result = cursor.fetchall()
        #print('Database successfully opened. Version is , ', result)
        #print('Table successfully created.')
    except conn.Error as error:
        print('Error inserting into Table', error)
    finally:
        if conn:
            conn.close()

insert_interns(interns_list)

#In sql you can have 
# TEXT --> FLOAT (DECIMAL)
# INTEGER --> INT (WHOLE NUMBER)
# REAL --> STRING (VARCHAR)
# BLOB --> 
# NULL --> NONE/DOES NOT EXIST
# the query is always in capital letters cause it is case sensitive
    # intern_id INTEGER PRIMARY KEY,
    #                     first_name TEXT NOT NULL,
    #                     last_name TEXT NOT NULL,
    #                     email TEXT,
    #                     phone_number TEXT,
    #                     school TEXT
# execute only executes the instance once but executemany does for a lot


