import sqlite3

conexao = sqlite3.connect("ddl.db")

cursor = conexao.cursor()

cursor.execute("ALTER TABLE USER DROP COLUMN telefone")

conexao.commit()

conexao.close()