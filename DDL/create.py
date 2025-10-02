import sqlite3

conexao = sqlite3.connect("ddl.db")

cursor = conexao.cursor()

cursor.executescript('''
            CREATE TABLE USER(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(200) UNIQUE NOT NULL,
                email VARCHAR(100),
                telefone VARCHAR(50)
            );
            CREATE TABLE PEDIDO(
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                pedido VARCHAE(200),
                id_usuario INTEGER,
                FOREIGN KEY (id_usuario) REFERENCES parent_table(id)
            );
''')

conexao.commit()

conexao.close()