import sqlite3


conexao = sqlite3.connect("dml.db")
cursor = conexao.cursor()

cursor.execute("UPDATE SOLICITANTE SET name = 'Arthur', email = 'arg@gmail.com' WHERE id = 20")
conexao.commit()
conexao.close()