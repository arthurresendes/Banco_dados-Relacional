import sqlite3


def uniao():
    conexao = sqlite3.connect("banco_union.db")
    
    cursor = conexao.cursor()
    
    cursor.execute('SELECT nome FROM USER UNION SELECT pedido FROM PEDIDO')
    linhas = cursor.fetchall()
    for i in linhas:
        print(i)
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    uniao()