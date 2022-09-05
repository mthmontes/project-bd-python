import sqlite3

newDataBase = sqlite3.connect('first_data.db')
cursor = newDataBase.cursor()

nameColumn = str(input('Qual coluna você quer remover?'))

removeColumn = f'ALTER TABLE people DROP COLUMN {nameColumn}'
cursor.execute(removeColumn)