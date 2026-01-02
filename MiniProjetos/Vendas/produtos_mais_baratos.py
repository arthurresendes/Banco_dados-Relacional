import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT p.nome, p.preco
    FROM PRODUTO as p
    ORDER BY p.preco ASC
    LIMIT 5
""")

res = cursor.fetchall()
for i in res:
    print(i)

conexao.close()