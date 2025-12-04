import sqlite3

conexao = sqlite3.connect("tigger.db")

cursor = conexao.cursor()


# Apenas um exemplo em sql server , no sqlite nao tem tiggers
cursor.execute("""
            CREATE TRIGGER tg_calcula_saldo
            ON VENDAS
            AFTER INSERT
            AS
            BEGIN
                UPDATE V
                SET novo_saldo = I.saldo_atual + I.valor_venda
                FROM VENDAS V
                JOIN inserted I ON V.id = I.id;
            END;
            GO
""")

conexao.commit()
conexao.close()