import sqlite3


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

def criacaoView():
    cursor.execute("""
        CREATE VIEW vwSelecaoTotal AS
          select round((vendas_qtd * valor_venda),2) as Valor_total
          from VENDEDOR;
        """)
    conexao.commit()
try:
    criacaoView()
except:
    print("View ja foi criada")
cursor.execute("SELECT * FROM vwSelecaoTotal")
res = cursor.fetchall()
for i in res:
    print(i)

conexao.commit()
conexao.close()