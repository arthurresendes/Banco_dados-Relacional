import sqlite3


conexao = sqlite3.connect("caracter.db")


cursor = conexao.cursor()


cursor.execute('''
            SELECT *
            FROM USERS
            WHERE SUBSTR(nome,1,4) = 'Arth';        
''')

consulta = cursor.fetchall()
for i in consulta:
    print(i)

conexao.commit()
conexao.close()