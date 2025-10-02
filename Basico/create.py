import sqlite3

conexao = sqlite3.connect("banco01.db")

cursor = conexao.cursor()

cursor.execute('''
            CREATE TABLE USERS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200),
                idade INT
            )
''')

conexao.commit()


conexao.close()