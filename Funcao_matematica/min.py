import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("SELECT nome,MIN((vendas_qtd*valor_venda)) FROM VENDEDOR")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()
