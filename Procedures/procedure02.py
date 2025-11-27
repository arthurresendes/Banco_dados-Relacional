'''
Isso é apenas um exemplo de procedure no sql server que nao funciona no sqlite3

'''


import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
   CREATE PROCEDURE BuscaPorNome
      @Nome VARCHAR(200)
    AS
    BEGIN
      SELECT * 
      FROM VENDEDOR
      where nome = @Nome
    END
    GO
""")

cursor.execute("EXECUTE BuscarPorNome @Nome = 'André Ribeiro';")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()