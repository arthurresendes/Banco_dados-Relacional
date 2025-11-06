import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
        SELECT strftime('%d/%m/%Y', 'now') AS data_hoje
""")
res = cursor.fetchall()
for i in res:
    print(i)

cursor.execute("""
        SELECT strftime('%H-%M', 'now') AS hora_atual
""")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()