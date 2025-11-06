import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
        SELECT nome, CAST(vendas_qtd AS FLOAT), valor_venda, round((vendas_qtd * valor_venda),2) AS total FROM VENDEDOR
""")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()