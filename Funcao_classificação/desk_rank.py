import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("SELECT nome , nome_venda , DENSE_RANK() OVER(ORDER BY valor_venda ASC) AS Maior_vendedor FROM VENDEDOR")

registro = cursor.fetchall()

for i in registro:
    print(i)

conexao.commit()
conexao.close()