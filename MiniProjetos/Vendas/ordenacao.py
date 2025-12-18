import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT vende.nome, vende.nome_venda, (vende.vendas_qtd * vende.valor_venda) AS total, clie.nome,clie.email
    FROM VENDA vd
    JOIN VENDEDOR vende
    ON vende.id = vd.id_vendedor
    JOIN CLIENTE clie
    ON clie.id = vd.id_cliente
    ORDER BY (vende.vendas_qtd * vende.valor_venda) DESC
    LIMIT 5
""")

res = cursor.fetchall()
for i in res:
    print(i)

conexao.close()