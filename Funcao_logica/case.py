import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
            SELECT nome , nome_venda, (vendas_qtd * valor_venda) AS total_venda,
            CASE
              WHEN (vendas_qtd * valor_venda) > 5000 then 'Caro'
              WHEN (vendas_qtd * valor_venda) BETWEEN 2000 and 5000 then 'Na faixa'
              ELSE 'barato'
            END AS categoria_preco
            FROM VENDEDOR             
""")

result = cursor.fetchall()

for i in result:
    print(i)

conexao.commit()
conexao.close()