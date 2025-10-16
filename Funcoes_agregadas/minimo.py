import sqlite3

conexao = sqlite3.connect("funcoes.db")

cursor = conexao.cursor()

cursor.execute("SELECT MIN(valor) as Menor_valor from PAGAMENTO")
result = cursor.fetchall()

for i in result:
    print(i)
conexao.commit()
conexao.close()