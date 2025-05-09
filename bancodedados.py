import mysql.connector
from datetime import datetime

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            password = 'Aluno123',
            database = 'projeto'
        )
        self.cursor = self.conexao.cursor()
        print('Conexao estabelecida')
        self.criar_tabelas()

    def criar_tabelas(self):
        comando_criar_produtos = '''
            CREATE TABLE IF NOT EXISTS produtos(   
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR (255) NOT NULL,
                descricao TEXT,
                quantidade INT NOT NULL,
                preco DECIMAL(10,2)NOT NULL
            )
        '''
        self.cursor.execute(comando_criar_produtos)
        

        comando_criar_vendas='''
            CREATE TABLE IF NOT EXISTS vendas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produto_id INT,
                quantidade INT NOT NULL,
                data_venda DATETIME NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES produtos(id)    
            )
        '''
        self.cursor.execute(comando_criar_vendas)
        self.conexao.commit()
        print('Tabelas criadas/verificadas com sucesso!')

bd = BancoDeDados()
