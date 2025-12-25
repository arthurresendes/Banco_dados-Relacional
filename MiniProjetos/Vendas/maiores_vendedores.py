import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT v.nome,c.email,v.nome_venda, v.vendas_qtd * v.valor_venda, ve.data_venda
    FROM VENDA as ve
    JOIN CLIENTE c
    ON ve.id_cliente = c.id 
    JOIN VENDEDOR v
    ON ve.id_vendedor = v.id 
    ORDER BY v.vendas_qtd * v.valor_venda DESC
    LIMIT 5
""")

res = cursor.fetchall()
for i in res:
    print(i)

conexao.close()
