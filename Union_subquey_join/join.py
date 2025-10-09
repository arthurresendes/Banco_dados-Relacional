import sqlite3

def juncao():
    conexao = sqlite3.connect("banco_union.db")
    cursor = conexao.cursor()
    
    cursor.execute('''
                SELECT
                  c.nome,
                  p.pedido
                FROM 
                 USER as c
                JOIN
                 PEDIDO as p
                 ON c.id = p.id_usuario   
    ''')
    linha = cursor.fetchall()
    for i in linha:
        print(i)

    conexao.commit()
    conexao.close()



if __name__ == "__main__":
    juncao()