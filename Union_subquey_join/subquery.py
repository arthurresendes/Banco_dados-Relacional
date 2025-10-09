import sqlite3


def sub():
    conexao = sqlite3.connect("banco_union.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('''
                SELECT
                   us.nome,
                   us.email,
                   P.pedido
                FROM
                  USER AS us
                JOIN
                  PEDIDO AS P
                  ON us.id = P.id_usuario;
    ''')
    linhas = cursor.fetchall()
    for i in linhas:
        print(i)
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    sub()