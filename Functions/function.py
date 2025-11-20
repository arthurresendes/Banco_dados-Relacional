import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

'''
Function em sqlite3 nao funciona , sendo assim isso é apenas um demonstrativo de conhecimento fazendo um procedure estilo sql manager

'''
# No returns decimal é o tipo de dado que irá voltar
cursor.execute("""
        CREATE FUNCTION CalcularTotal(
            preco REAL,
            quantidade INT
        )
        RETURNS REAL 
        AS
        BEGIN
            RETURN preco * quantidade;
END;
GO
""")

cursor.execute("SELECT dbo.CalcularTotal(50.5054, 3);")
cursor.execute('''
            SELECT nome, dbo.CalcularTotal(valor_venda,vendas_qtd) AS preco_total
            FROM vendedor
            WHERE id = 1;
''')

conexao.commit()
conexao.close()