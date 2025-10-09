import sqlite3


def insercao():
    conexao = sqlite3.connect("banco_union.db")
    
    cursor = conexao.cursor()
    
    lista_nomes = [('Alice', 'alice@exemplo.com'), 
                   ('Bob', 'bob@exemplo.com'), 
                   ('Carlos', 'carlos@exemplo.com')]
    cursor.executemany("INSERT INTO USER (nome, email) VALUES (?,?)",lista_nomes)
    
    lista_pedido = [
        ("Cafe", 1),
        ("Arroz", 2),
        ("Feijão", 3)
    ]
    
    cursor.executemany("INSERT INTO PEDIDO (pedido, id_usuario) VALUES (?,?)", lista_pedido)
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    insercao()