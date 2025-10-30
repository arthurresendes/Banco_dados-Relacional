import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


cursor.execute("""
        CREATE TABLE VENDEDOR(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(200),
            nome_venda VARCHAR(100),
            vendas_qtd INTEGER,
            valor_venda REAL
        );
""")

conexao.commit()
conexao.close()

