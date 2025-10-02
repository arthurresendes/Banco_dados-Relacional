import sqlite3


conexao = sqlite3.connect("dml.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM SOLICITANTE WHERE id = 11;")
resultado1 = cursor.fetchall()
cursor.execute("SELECT * FROM SOLICITANTE WHERE id = 20;")
resultado2 = cursor.fetchall()
cursor.execute("SELECT * FROM SOLICITANTE WHERE id = 1;")
resultado3 = cursor.fetchall()

lista_selects = [resultado1,resultado2,resultado3]
for i in lista_selects:
    print(i)


conexao.commit()
conexao.close()