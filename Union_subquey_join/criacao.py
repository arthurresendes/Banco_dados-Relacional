import sqlite3

def criacao():
    conexao = sqlite3.connect("banco_union.db")
    
    cursor = conexao.cursor()
    
    cursor.executescript('''
            CREATE TABLE IF NOT EXISTS USER(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(200),
                email VARCHAR(50)  
            );
            CREATE TABLE IF NOT EXISTS PEDIDO(
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido VARCHAR(200),
                id_usuario INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES USER(id)  
            );
    ''')
    
    conexao.commit()
    conexao.close()


if __name__ == "__main__":
    criacao()
