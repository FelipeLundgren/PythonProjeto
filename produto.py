produtos = []
class Produto:
    def __init__(self,nome,descricao,quantidade_disponivel,preco,id=None):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.quantidade_disponivel = quantidade_disponivel
        self.preco = preco

