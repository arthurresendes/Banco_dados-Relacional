import sqlite3

def criando_tabela():
    conexao = sqlite3.connect("dml.db")
    cursor = conexao.cursor()
    
    cursor.executescript('''
                CREATE TABLE SOLICITANTE(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(200),
                    email VARCHAR(50)
                );
                
                CREATE TABLE CHAMADO(
                    id_chamado INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo VARCHAR(50),
                    id_solicitante INTEGER,
                    FOREIGN KEY (id_solicitante) REFERENCES SOLICITANTE(id)
                );
    ''')
    
    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criando_tabela()