import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

# Nao funciona por aqui nativamente em sqlite3 mas funciona em servidores
cursor.execute("""
        select charset(nome) from VENDEDOR where id = 2
""")

conexao.commit()
conexao.close()