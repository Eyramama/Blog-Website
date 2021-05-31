import sqlite3

try:  
        conn = sqlite3.connect('Provision_store3.db')
        cursor = conn.cursor()
        query = """ DELETE FROM ProvisionStore WHERE product_id = 4"""
        cursor.execute(query)
        conn.commit()
        #results = cursor.fetchall()
        print("Data deleted successfully!")
        # for interns in results:
        #     print('name: ', interns[0])
        #     print('price: ', interns[1])
        #     print('\n')
except conn.Error as error:
        print('Error returning data from Table', error)
finally:
        if conn:
            conn.close()