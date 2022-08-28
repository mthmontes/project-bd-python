import sqlite3

newDataBase = sqlite3.connect('first_data.db')
cursor = newDataBase.cursor()

cursor.execute('SELECT * FROM people')

for dados in cursor.fetchall():
    print(dados)
    
newDataBase.close()