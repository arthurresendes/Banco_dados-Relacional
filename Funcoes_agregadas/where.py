import sqlite3

conexao = sqlite3.connect("funcoes.db")

cursor = conexao.cursor()

cursor.execute('''
            SELECT 
              nome , COUNT(id) as total_pessoas
            FROM 
              USERS
            WHERE nome = 'Daniel Souza'
''')
result = cursor.fetchall()

for i in result:
    print(i)
conexao.commit()
conexao.close()