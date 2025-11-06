import sqlite3
from datetime import datetime


conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

dados_vendedores = [
    ("Maria Souza", "Notebook XPTO", 2, 8500.50, data_atual),
    ("João Silva", "Teclado RGB", 5, 499.90, data_atual),
    ("Ana Paula", "Mouse Gamer", 1, 150.00, data_atual),
    ("Pedro Gomes", "Monitor 4K", 1, 3500.00, data_atual),
    ("Laura Costa", "Webcam HD", 3, 299.70, data_atual),
    ("Ricardo Lima", "Cadeira Gamer", 2, 1899.00, data_atual),
    ("Camila Torres", "Headset Sem Fio", 4, 1200.00, data_atual),
    ("Fernanda Alves", "HD Externo 1TB", 3, 899.90, data_atual),
    ("Rafael Santos", "Impressora Laser", 1, 2100.00, data_atual),
    ("Juliana Nunes", "SSD 1TB", 2, 950.00, data_atual),
    ("Lucas Pereira", "Caixa de Som Bluetooth", 6, 780.00, data_atual),
    ("Gabriel Costa", "Fonte 650W", 2, 500.00, data_atual),
    ("Sofia Martins", "Microfone Condensador", 1, 650.00, data_atual),
    ("André Ribeiro", "Mousepad XXL", 3, 180.00, data_atual),
    ("Patrícia Dias", "Placa de Vídeo RTX 4060", 1, 2999.99, data_atual),
    ("Marcos Silva", "Roteador Wi-Fi 6", 2, 1300.00, data_atual),
    ("Aline Rocha", "Notebook Slim", 1, 7200.00, data_atual),
    ("Eduardo Moreira", "Teclado Mecânico", 4, 999.00, data_atual),
    ("Bruna Ferreira", "Pen Drive 128GB", 10, 350.00, data_atual),
    ("Carlos Henrique", "Monitor Curvo", 2, 4200.00, data_atual)
]

cursor.executemany("""
    INSERT INTO VENDEDOR (nome, nome_venda, vendas_qtd, valor_venda, data_venda)
    VALUES (?, ?, ?, ?, ?)
""", dados_vendedores)

conexao.commit()
conexao.close()