import sqlite3

newDataBase = sqlite3.connect('first_data.db')
cursor = newDataBase.cursor()

addColumn = 'ALTER TABLE people ADD COLUMN mail varchar(32)'
cursor.execute(addColumn)