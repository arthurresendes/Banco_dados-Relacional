import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT v.nome,v.nome_venda, v.vendas_qtd * v.valor_venda
    FROM VENDEDOR as v
    ORDER BY v.vendas_qtd * v.valor_venda DESC
    LIMIT 5
""")

res = cursor.fetchall()
for i in res:
    print(i)

conexao.close()
