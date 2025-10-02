import sqlite3

conexao = sqlite3.connect("banco01.db")

cursor = conexao.cursor()

cursor.execute('''
            ALTER TABLE USERS
            ADD email VARCHAR(100);
''')

conexao.commit()


conexao.close()
