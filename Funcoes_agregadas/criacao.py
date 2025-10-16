import sqlite3

conexao  = sqlite3.connect("funcoes.db")

cursor = conexao.cursor()

cursor.executescript("""
                CREATE TABLE USERS(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome VARCHAR(200),
                   email VARCHAR(50)   
                );  
                
                CREATE TABLE PAGAMENTO(
                    id_pay INTEGER PRIMARY KEY AUTOINCREMENT,
                    produto VARCHAR(100),
                    valor REAL,
                    id_usuario INTEGER,
                    FOREIGN KEY (id_usuario) REFERENCES USERS(id) 
                );                
""")

conexao.commit()
conexao.close()