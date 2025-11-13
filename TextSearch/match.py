import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

'''
Em mysql funcionaria assim , porem como estamos no sqlite3 usamos o like
cursor.execute("SELECT * FROM VENDEDOR WHERE MATCH(nome_venda) AGAINST('Notebook')")
'''

cursor.execute("SELECT * FROM VENDEDOR WHERE nome_venda LIKE '%Notebook%'")
res = cursor.fetchall()
for i in res:
    print(i)
conexao.commit()
conexao.close()