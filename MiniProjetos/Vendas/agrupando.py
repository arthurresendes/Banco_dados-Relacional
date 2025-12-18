import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT nome, preco,count(nome)
    FROM PRODUTO
    GROUP BY nome
    LIMIT 5
""")

res = cursor.fetchall()
for i in res:
    print(i)

conexao.close()
