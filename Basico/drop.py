import sqlite3


conexao = sqlite3.connect("banco01.db")

cursor = conexao.cursor()

cursor.execute('''
            ALTER TABLE USERS
            DROP COLUMN idade;
''')


conexao.commit()

conexao.close()