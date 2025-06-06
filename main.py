from sistema import*
from produto import*
from vendas import*
from bancodedados import*

op = ''
sistema = Sistema()

while True:
    print('-------------MENU-------------')
    print('1- Cadastrar um novo produto')
    print('2- Cadastrar uma nova venda')
    print('3- Listar produtos em estoque')
    print('4- Listar vendas')
    print('5- Alterar quantidade de produtos')
    print('6- Deletar produto')
    print('7- Sair do menu')
    op = int(input('Digite uma opção: '))
    if op == 1:
        item = Produto(
            input('Digite o nome do produto: '),
            input('Digite a descrição do produto:'),
            int(input('Digite a quantidade disponivel: ')),
            float(input('Digite o valor do produto: '))
            )
        sistema.adicionar_produto(item)
    elif op == 2:
        venda = Vendas(
            id = int(input('Digite o ID da venda:')),
            id_produto = int(input('Digite o ID do produto vendido: ')),
            quantidade_vendida = int(input('Digite a quantidade vendida:')),
            data_venda = input('Digite a data da venda: ')
            )
        print(venda)
        sistema.cadastrar_venda(venda)
    elif op == 3:

        produtos = sistema.listar_produtos()
        for produto in produtos:
            print(f'ID: {produto.id}')
            print(f'Nome: {produto.nome}')
            print(f'Descricao: {produto.descricao}')
            print(f'Quantidade: {produto.quantidade}')
            print(f'Preco: {produto.preco}')
            print(f'--------------------------------')
    elif op == 4:
        sistema.listar_vendas()

    elif op == 5:
        sistema.alterar_quantidade_produtos(id)

    elif op == 6:
        sistema.deletar_produto(id)
    
    elif op == 7:
        break
    
    else:
        print('Opcao invalida')