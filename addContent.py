import sqlite3

try:
    newDataBase = sqlite3.connect('first_data.db')
    cursor = newDataBase.cursor()

    name = str(input("Enter your name: "))
    age = int(input("Enter your age: "))
    id = int(input("Enter ID: "))
    mail = str(input('Enter your best mail: '))

    cursor.execute('INSERT INTO people (name, age, id, mail) VALUES (?, ?, ?, ?)',
                (name, age, id, mail))

    newDataBase.commit()
    print("Add content in database is successfully.")
    
except ValueError:
    print("Failed!")
    