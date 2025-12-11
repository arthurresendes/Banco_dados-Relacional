import sqlite3
from datetime import datetime

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()


dados_vendedores = [
    ("Maria Souza", "Notebook XPTO", 2, 8500.50),
    ("João Silva", "Teclado RGB", 5, 499.90),
    ("Ana Paula", "Mouse Gamer", 1, 150.00),
    ("Pedro Gomes", "Monitor 4K", 1, 3500.00),
    ("Laura Costa", "Webcam HD", 3, 299.70),
    ("Ricardo Lima", "Cadeira Gamer", 2, 1899.00),
    ("Camila Torres", "Headset Sem Fio", 4, 1200.00),
    ("Fernanda Alves", "HD Externo 1TB", 3, 899.90),
    ("Rafael Santos", "Impressora Laser", 1, 2100.00),
    ("Juliana Nunes", "SSD 1TB", 2, 950.00),
    ("Lucas Pereira", "Caixa de Som Bluetooth", 6, 780.00),
    ("Gabriel Costa", "Fonte 650W", 2, 500.00),
    ("Sofia Martins", "Microfone Condensador", 1, 650.00),
    ("André Ribeiro", "Mousepad XXL", 3, 180.00),
    ("Patrícia Dias", "Placa de Vídeo RTX 4060", 1, 2999.99),
    ("Marcos Silva", "Roteador Wi-Fi 6", 2, 1300.00),
    ("Aline Rocha", "Notebook Slim", 1, 7200.00),
    ("Eduardo Moreira", "Teclado Mecânico", 4, 999.00),
    ("Bruna Ferreira", "Pen Drive 128GB", 10, 350.00),
    ("Carlos Henrique", "Monitor Curvo", 2, 4200.00)
]

cursor.executemany("INSERT INTO VENDEDOR(nome,nome_venda,vendas_qtd,valor_venda) VALUES (?,?,?,?)", dados_vendedores)

dados_clientes = [
    ("Lucas Andrade", "lucas@gmail.com"),
    ("Fernanda Souza", "fernanda@gmail.com"),
    ("Marcos Paulo", "marcos@gmail.com"),
    ("Carla Ribeiro", "carla@gmail.com"),
    ("João Pedro", "jp@gmail.com"),
    ("Bruna Martins", "bruna@gmail.com"),
    ("Thiago Santos", "thiago@gmail.com"),
    ("Aline Silva", "aline@gmail.com"),
    ("Gustavo Torres", "gustavo@gmail.com"),
    ("Patrícia Moura", "patricia@gmail.com")
]

cursor.executemany(
    "INSERT INTO CLIENTE(nome, email) VALUES (?,?)",
    dados_clientes
)


dados_produtos = [
    ("Notebook XPTO", 4300.00),
    ("Teclado RGB", 250.00),
    ("Mouse Gamer", 150.00),
    ("Monitor 4K", 1800.00),
    ("Webcam HD", 130.00),
    ("Cadeira Gamer", 950.00),
    ("Headset Sem Fio", 300.00),
    ("HD Externo 1TB", 420.00),
    ("Impressora Laser", 1100.00),
    ("SSD 1TB", 500.00)
]

cursor.executemany(
    "INSERT INTO PRODUTO(nome, preco) VALUES (?,?)",
    dados_produtos
)


dados_vendas = [
    (1, 1, 1, 1, "2025-01-02"),
    (2, 2, 3, 2, "2025-01-05"),
    (3, 3, 2, 1, "2025-01-10"),
    (4, 4, 4, 1, "2025-01-12"),
    (5, 5, 5, 3, "2025-01-15"),
    (6, 6, 6, 1, "2025-01-18"),
    (7, 7, 7, 4, "2025-01-20"),
    (8, 8, 8, 2, "2025-01-22"),
    (9, 9, 9, 1, "2025-01-25"),
    (10, 10, 10, 3, "2025-01-28")
]

cursor.executemany(
    "INSERT INTO VENDA(id_vendedor, id_cliente, id_produto, quantidade, data_venda) VALUES (?,?,?,?,?)",
    dados_vendas
)


conexao.commit()
conexao.close()

print("Inserções concluídas com sucesso!")
