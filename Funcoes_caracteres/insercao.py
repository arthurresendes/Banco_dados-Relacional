import sqlite3


conexao = sqlite3.connect("caracter.db")


cursor = conexao.cursor()
usuarios = [
    ("Arthur Resende", "arthur.resende@gmail.com", 20),
    ("Beatriz Lima", "beatriz.lima@gmail.com", 22),
    ("Carlos Souza", "carlos.souza@gmail.com", 25),
    ("Daniela Rocha", "daniela.rocha@gmail.com", 19),
    ("Eduardo Castro", "eduardo.castro@gmail.com", 27),
    ("Fernanda Alves", "fernanda.alves@gmail.com", 23),
    ("Gabriel Santos", "gabriel.santos@gmail.com", 21),
    ("Helena Martins", "helena.martins@gmail.com", 24),
    ("Igor Oliveira", "igor.oliveira@gmail.com", 28),
    ("Juliana Mendes", "juliana.mendes@gmail.com", 26),
    ("Kauan Ribeiro", "kauan.ribeiro@gmail.com", 18),
    ("Larissa Costa", "larissa.costa@gmail.com", 29),
    ("Marcelo Gomes", "marcelo.gomes@gmail.com", 30),
    ("Natália Ferreira", "natalia.ferreira@gmail.com", 19),
    ("Otávio Lima", "otavio.lima@gmail.com", 22),
    ("Patrícia Nunes", "patricia.nunes@gmail.com", 25),
    ("Rafael Duarte", "rafael.duarte@gmail.com", 23),
    ("Sabrina Moraes", "sabrina.moraes@gmail.com", 21),
    ("Thiago Pires", "thiago.pires@gmail.com", 20),
    ("Ursula Reis", "ursula.reis@gmail.com", 24),
    ("Victor Carvalho", "victor.carvalho@gmail.com", 27),
    ("Wesley Silva", "wesley.silva@gmail.com", 28),
    ("Ximena Prado", "ximena.prado@gmail.com", 26),
    ("Yasmin Lopes", "yasmin.lopes@gmail.com", 19),
    ("Zeca Moreira", "zeca.moreira@gmail.com", 29),
    ("Alana Figueiredo", "alana.figueiredo@gmail.com", 22),
    ("Bruno Rocha", "bruno.rocha@gmail.com", 23),
    ("Caio Tavares", "caio.tavares@gmail.com", 24),
    ("Diana Luz", "diana.luz@gmail.com", 25),
    ("Elisa Prado", "elisa.prado@gmail.com", 26)
]


cursor.executemany("INSERT INTO USERS (nome,email,idade) VALUES(?,?,?)", usuarios)

conexao.commit()
conexao.close()