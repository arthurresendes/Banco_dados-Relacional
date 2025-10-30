import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT nome FROM VENDEDOR WHERE (vendas_qtd * valor_venda) BETWEEN 2000 and 4000")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()