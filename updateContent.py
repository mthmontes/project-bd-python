import sqlite3

try:
    newDataBase = sqlite3.connect('first_data.db')
    cursor = newDataBase.cursor()

    id = int(input("Enter ID to update: "))
    newName = str(input("Enter a new name: "))
    newAge = int(input("Enter a new age: "))

    cursor.execute('UPDATE people SET name = ?, age = ? WHERE id = ?', (newName, newAge, id))

    newDataBase.commit()
    
    print("Updated is a successful!")

except ValueError:
    print("Error updating.")

