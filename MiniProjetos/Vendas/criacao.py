import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS VENDEDOR(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(200),
        nome_venda VARCHAR(100),
        vendas_qtd INTEGER,
        valor_venda REAL
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS CLIENTE(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(200),
        email VARCHAR(150) UNIQUE
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUTO(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(150),
        preco REAL
    );
""")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS VENDA(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_vendedor INTEGER,
        id_cliente INTEGER,
        id_produto INTEGER,
        quantidade INTEGER,
        data_venda TEXT,
        FOREIGN KEY(id_vendedor) REFERENCES VENDEDOR(id),
        FOREIGN KEY(id_cliente) REFERENCES CLIENTE(id),
        FOREIGN KEY(id_produto) REFERENCES PRODUTO(id)
    );
""")

conexao.commit()
conexao.close()
