import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
        SELECT nome, strftime('%d/%m/%Y', data_venda) AS data_formatada
        FROM VENDEDOR;
""")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()