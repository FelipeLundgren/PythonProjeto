from produto import*
from vendas import*
from bancodedados import*
class Sistema:
    def __init__(self):
        self.bd = BancoDeDados()
        self.vendas = []


    def adicionar_produto(self,produto):
        if not produto.nome or produto.quantidade < 0 or produto.preco <=0:
            print('Dados do produto invalidos')
            return None
        comando = '''   
            INSERT INTO produtos(nome,descricao,quantidade,preco)
            VALUES (%s,%s,%s,%s)
    '''
        dados = (produto.nome,produto.descricao, produto.quantidade, produto.preco)   
    
        self.bd.cursor.execute(comando,dados)
        self.bd.conexao.commit()
        novo_id = self.bd.cursor.lastrowid
        print(f'Produto {produto.nome} adicionado com sucesso')

    def cadastrar_venda(self,venda):
        self.vendas.append(venda)

    def listar_produtos(self):
        for i in self.produtos:
            print(f'''id: {i.id} \n
                Nome: {i.nome}\n
                Descricao: {i.descricao}\n
                Quantidade disponivel: {i.quantidade_disponivel}\n
                Preco do produto: {i.preco}
                ''')
    def listar_vendas(self):
        for i in self.vendas:
             print(f'''ID venda: {i.id} \n
                Id produto: {i.id_produto}\n
                Quantidade de vendas: {i.quantidade_vendida}\n
                Data da venda: {i.data_venda}
                ''')
            
    def alterar_quantidade_produtos(self,id):
        for i in self.produtos:
            if i.id == id:
                print(f'Quantidade de produto: {i.quantidade_disponivel}\n')
                novo_valor = int(input('Qual a nova quantidade disponivel?'))
                i.quantidade_disponivel = novo_valor
                print(f'A nova quantidade disponivel é: {i.quantidade_disponivel}')
        else:
            print('ID nao encontrado')
    
    def deletar_produto(self,id):
        for i in self.produtos:
            if i.id == id:
                escolha = input(f'Deseja deletar o produto:{i.nome}? s/n')
                if escolha == 's':
                    self.produtos.remove(i)
                    print('Produto deletado com sucesso')
                elif escolha == 'n':
                    print('Produto nao deletado')
        else:
            print('ID nao encontrado')

    
            
            