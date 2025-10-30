import sqlite3


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

conexao.commit()
conexao.close()