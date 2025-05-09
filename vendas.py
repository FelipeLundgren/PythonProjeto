from datetime import datetime
vendas = []
class Vendas:
    def __init__(self,id,id_produto,quantidade_vendida):
        self.id = id
        self.id_produto = id_produto
        self.quantidade_vendida = quantidade_vendida
        self.data_venda = datetime.now()
        