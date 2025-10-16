import sqlite3

conexao  = sqlite3.connect("funcoes.db")

cursor = conexao.cursor()

cursor.execute("SELECT COUNT(*) FROM USERS")
result = cursor.fetchall()

for i in result:
    print(i)
conexao.commit()
conexao.close()