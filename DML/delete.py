import sqlite3


conexao = sqlite3.connect("dml.db")
cursor = conexao.cursor()

cursor.execute("DELETE FROM SOLICITANTE WHERE id = 10;")
conexao.commit()
conexao.close()