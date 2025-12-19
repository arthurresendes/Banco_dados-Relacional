import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT v.nome, v.valor_venda
    FROM vendedor v
    WHERE EXISTS (
    SELECT 1
    FROM produto p
    WHERE v.valor_venda > p.preco
);
""")

res = cursor.fetchall()
for i in res:
    print(i)

conexao.close()