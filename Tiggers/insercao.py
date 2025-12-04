import sqlite3
import random

conexao = sqlite3.connect("tigger.db")
cursor = conexao.cursor()

insercoes = []

saldo = 1000.00

for _ in range(30):
    valor_venda = round(random.uniform(50, 500), 2)
    novo_saldo = round(saldo + valor_venda, 2)

    insercoes.append((saldo, valor_venda, novo_saldo))

    saldo = novo_saldo 

cursor.executemany("""
    INSERT INTO VENDAS (saldo_atual, valor_venda, novo_saldo)
    VALUES (?, ?, ?)
""", insercoes)

conexao.commit()
conexao.close()

print("30 inserções feitas com sucesso!")
