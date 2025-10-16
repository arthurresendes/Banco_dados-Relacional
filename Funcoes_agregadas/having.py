import sqlite3

conexao = sqlite3.connect("funcoes.db")

cursor = conexao.cursor()

cursor.execute('''
            SELECT 
              produto , COUNT(id_pay) as total_produtos
            FROM 
              PAGAMENTO
            GROUP BY 
              produto
            HAVING
              total_produtos = 1
''')
result = cursor.fetchall()

for i in result:
    print(i)
conexao.commit()
conexao.close()