import sqlite3

def update_phone_number(id, new):
    try:  
            conn = sqlite3.connect('internship_demo.db')
            cursor = conn.cursor()
            query = """UPDATE interns SET phone_number = ? WHERE intern_id = ?"""
            data_tuple = (new, id)
            cursor.execute(query, data_tuple)
            conn.commit()
            #results = cursor.fetchall()
            results = cursor.fetchall()
            print("Data updated successfully!", results)
    #         for interns in results:
    #             print('firstname: ', interns[0])
    #             print('lastname: ', interns[1])
    #             print('\n')
    except conn.Error as error:
            print('Error returning data from Table', error)
    finally:
            if conn:
                conn.close()

update_phone_number(1, "2345678910")