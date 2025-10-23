import sqlite3


conexao = sqlite3.connect("caracter.db")


cursor = conexao.cursor()


cursor.execute('''
            CREATE TABLE USERS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT UNIQUE,
                idade INTEGER
            )               
''')

conexao.commit()
conexao.close()