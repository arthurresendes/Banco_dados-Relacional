import sqlite3


conexao = sqlite3.connect("caracter.db")


cursor = conexao.cursor()

# Position no sqlite é instr
cursor.execute('''
            SELECT nome, INSTR(nome , 'a')
            FROM USERS
            WHERE LENGTH(nome) > 10;        
''')

consulta = cursor.fetchall()
for i in consulta:
    print(i)

conexao.commit()
conexao.close()