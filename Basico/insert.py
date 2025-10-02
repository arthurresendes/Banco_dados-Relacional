import sqlite3


conexao = sqlite3.connect("banco01.db")

cursor = conexao.cursor()

lista_pessoas = [
    ("Davi", "davi@gmail.com"),
    ("Mateus", "mateus@gmail.com"),
    ("Henrique", "henrique@gmail.com")
]

# executemany para varios e execute para um só
cursor.executemany("INSERT INTO USERS (nome,email) VALUES(?,?)", lista_pessoas)

conexao.commit()

conexao.close()