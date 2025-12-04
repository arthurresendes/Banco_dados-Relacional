import sqlite3

conexao = sqlite3.connect("tigger.db")

cursor = conexao.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS VENDAS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                saldo_atual DECIMAL(10,2),
                valor_venda DECIMAL(10,2),
                novo_saldo DECIMAL(10,2)
            );
""")

conexao.commit()
conexao.close()