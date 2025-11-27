'''
Isso é apenas um exemplo de procedure no sql server que nao funciona no sqlite3

'''


import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
   CREATE FUNCTION TotalVenda(qtd INT , valor_venda REAL)
   RETURNS DECIMAL(10,2)
   AS
   BEGIN
     RETURN qtd * valor_venda;
    END
    GO
""")

cursor.execute("SELECT TotalVenda(vendas_qtd,valor_venda) AS Total where id = 1")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()

