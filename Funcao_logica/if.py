import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT nome, IF(vendas_qtd >= 5, 'Produto com bastante quantidade', 'Produto com pouca quantidade') FROM VENDEDOR")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()