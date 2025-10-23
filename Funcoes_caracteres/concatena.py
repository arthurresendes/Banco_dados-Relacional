import sqlite3


conexao = sqlite3.connect("caracter.db")


cursor = conexao.cursor()


cursor.execute('''
            SELECT CONCAT(nome , ' ' , email) AS nome_email
            FROM USERS
            WHERE SUBSTR(nome,1,1) = 'A';        
''')

consulta = cursor.fetchall()
for i in consulta:
    print(i)

conexao.commit()
conexao.close()