import sqlite3

try:
    newDataBase = sqlite3.connect('first_data.db')
    cursor = newDataBase.cursor()
    
    remove_id = int(input('Input a ID for remove: '))
    cursor.execute(f'DELETE FROM people WHERE id = {remove_id}')

    newDataBase.commit()
    newDataBase.close()
    print("Data removed successfully.")
    
except sqlite3.Error as err:
    print("Error detected: ", err)
