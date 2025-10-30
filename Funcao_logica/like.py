import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT nome FROM VENDEDOR WHERE nome LIKE '%a'")

#cursor.execute("SELECT nome FROM VENDEDOR WHERE nome LIKE 'a%'")

#cursor.execute("SELECT nome FROM VENDEDOR WHERE nome LIKE 'A_a'")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()