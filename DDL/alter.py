import sqlite3

conexao = sqlite3.connect("ddl.db")

cursor = conexao.cursor()

cursor.execute("ALTER TABLE USER ADD COLUMN CPF VARCHAR(15);")

conexao.commit()

conexao.close()