import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()
# arredonda com round e pega a base que sera o total venda e o expoente é 2
cursor.execute("SELECT nome,(vendas_qtd*valor_venda) AS total_venda, round(power((vendas_qtd*valor_venda), 2), 2) FROM VENDEDOR")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()