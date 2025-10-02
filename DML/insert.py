import sqlite3


conexao = sqlite3.connect("dml.db")
cursor = conexao.cursor()

lista_solicitantes = [
    ("Ana Souza", "ana.souza@example.com"),
    ("Bruno Lima", "bruno.lima@example.com"),
    ("Carla Mendes", "carla.mendes@example.com"),
    ("Diego Ferreira", "diego.ferreira@example.com"),
    ("Eduarda Silva", "eduarda.silva@example.com"),
    ("Felipe Costa", "felipe.costa@example.com"),
    ("Gabriela Rocha", "gabriela.rocha@example.com"),
    ("Henrique Alves", "henrique.alves@example.com"),
    ("Isabela Martins", "isabela.martins@example.com"),
    ("João Pereira", "joao.pereira@example.com"),
    ("Kamila Azevedo", "kamila.azevedo@example.com"),
    ("Lucas Oliveira", "lucas.oliveira@example.com"),
    ("Mariana Gomes", "mariana.gomes@example.com"),
    ("Nicolas Andrade", "nicolas.andrade@example.com"),
    ("Olívia Fernandes", "olivia.fernandes@example.com"),
    ("Pedro Cardoso", "pedro.cardoso@example.com"),
    ("Rafaela Pinto", "rafaela.pinto@example.com"),
    ("Samuel Barros", "samuel.barros@example.com"),
    ("Thiago Ribeiro", "thiago.ribeiro@example.com"),
    ("Vitória Teixeira", "vitoria.teixeira@example.com")
]

cursor.executemany("INSERT INTO SOLICITANTE (name,email) VALUES (?,?)",lista_solicitantes)
conexao.commit()
conexao.close()