import sqlite3

newDataBase = sqlite3.connect('first_data.db')
cursor = newDataBase.cursor()

addTabela = str(input("Qual coluna você quer adicionar a tabela?"))

addColumn = f'ALTER TABLE people ADD COLUMN {addTabela} varchar(32)'
cursor.execute(addColumn)