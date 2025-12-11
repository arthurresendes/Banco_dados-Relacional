import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE VIEW selectTotal AS
      select vendo.nome,vendo.vendas_qtd,vendo.valor_venda, round(vendo.valor_venda * vendo.vendas_qtd,2), cli.nome,prod.nome,prod.preco,venda.data_venda
      FROM venda 
      JOIN vendedor as vendo
      ON vendo.id = venda.id_vendedor
      JOIN cliente as cli
      ON cli.id = venda.id_cliente
      JOIN produto as prod
      ON prod.id = venda.id_produto
""")
conexao.commit()
cursor.execute("SELECT * FROM selectTotal")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()