import sqlite3

conexao  = sqlite3.connect("funcoes.db")

cursor = conexao.cursor()
usuarios = [
    ("Ana Silva", "ana.silva@email.com"),
    ("Bruno Costa", "bruno.costa@email.com"),
    ("Carla Mendes", "carla.mendes@email.com"),
    ("Daniel Souza", "daniel.souza@email.com"),
    ("Eduarda Lima", "eduarda.lima@email.com"),
    ("Felipe Torres", "felipe.torres@email.com"),
    ("Gabriela Rocha", "gabriela.rocha@email.com"),
    ("Henrique Alves", "henrique.alves@email.com"),
    ("Isabela Nunes", "isabela.nunes@email.com"),
    ("João Carvalho", "joao.carvalho@email.com"),
    ("Karen Duarte", "karen.duarte@email.com"),
    ("Lucas Ferreira", "lucas.ferreira@email.com"),
    ("Mariana Oliveira", "mariana.oliveira@email.com"),
    ("Natália Barbosa", "natalia.barbosa@email.com"),
    ("Otávio Ramos", "otavio.ramos@email.com"),
    ("Patrícia Martins", "patricia.martins@email.com"),
    ("Ricardo Gonçalves", "ricardo.goncalves@email.com"),
    ("Sofia Pires", "sofia.pires@email.com"),
    ("Thiago Castro", "thiago.castro@email.com"),
    ("Vitória Fernandes", "vitoria.fernandes@email.com")
]
cursor.executemany("INSERT INTO USERS(nome,email) VALUES(?,?)", usuarios)
pagamentos = [
    ("Teclado Mecânico", 350.00, 1),
    ("Mouse Gamer", 250.00, 2),
    ("Monitor 27''", 1200.00, 3),
    ("Headset Bluetooth", 430.00, 4),
    ("Notebook Dell", 4200.00, 5),
    ("Cadeira Gamer", 950.00, 6),
    ("SSD 1TB", 520.00, 7),
    ("Placa de Vídeo RTX 4060", 2800.00, 8),
    ("Fonte 750W", 480.00, 9),
    ("Gabinete RGB", 390.00, 10),
    ("Teclado sem fio", 220.00, 11),
    ("Mousepad Grande", 85.00, 12),
    ("Monitor Curvo 32''", 1600.00, 13),
    ("HD Externo 2TB", 380.00, 14),
    ("Impressora HP", 720.00, 15),
    ("Tablet Samsung", 2100.00, 16),
    ("Smartphone", 3200.00, 17),
    ("Relógio Inteligente", 690.00, 18),
    ("Cabo HDMI 2.1", 90.00, 19),
    ("Caixa de Som Bluetooth", 310.00, 20)
]
cursor.executemany("INSERT INTO PAGAMENTO(produto,valor,id_usuario) VALUES(?,?,?)",pagamentos)
cursor.execute("INSERT INTO USERS(nome,email) VALUES(?,?)", ("Daniel Souza", "daniel.souza@email.com"))

conexao.commit()
conexao.close()
