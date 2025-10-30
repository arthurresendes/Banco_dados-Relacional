import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT nome,ROUND((vendas_qtd*valor_venda),2) FROM VENDEDOR")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()