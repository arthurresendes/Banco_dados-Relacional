import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

'''
Procedures em sqlite3 nao funciona , sendo assim isso é apenas um demonstrativo de conhecimento fazendo um procedure estilo sql manager

'''

cursor.execute("""
        CREATE PROCEDURE RetornaTotalVenda
            @idVendedor int
        AS
        BEGIN
            SELECT
            nome,
            vendas_qtd * valor_venda AS total_venda
        FROM
            VENDEDOR
        where 
            id = @idVendedor
END;
GO
""")

cursor.execute("EXEC RetornaTotalVenda @idVendedor = 1")

conexao.commit()
conexao.close()