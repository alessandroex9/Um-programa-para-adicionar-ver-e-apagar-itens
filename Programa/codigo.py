"""
Faça uma lista de compras com lista
O usúario deve ter a possibilidade de
inserir, apagar e listar os valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

compras = []

while True:
    print('Selecione uma opcão')
    opcao_usuario = input('[i]nserir [a]pagar [l]ista: ')

    if opcao_usuario == 'i':
            novo_item = input('Digite o novo item: ')
            compras.append(novo_item)
            print('Item inserido com sucesso!')
            print('-' * 25)
                
    elif opcao_usuario == 'a':
        if not compras:
            print('A lista de compras está vazia!')
            continue
        print('Lista de compras:')
        for indice, item in enumerate(compras):
            print(indice, item)
        
        escolha = input('Selecione o número do item que deseja apagar: ')
        try:
            indice_escolhido = int(escolha)
            if indice_escolhido < 0 or indice_escolhido >= len(compras):
                print('Índice inválido!')
            else:
                del compras[indice_escolhido]
                print('Item removido com sucesso!')
        except ValueError:
            print('Opção inválida!')

        print('-' * 25)

    elif opcao_usuario == 'l':
        if not compras:
            print('A lista de compras está vazia!')
        else:
            print('Lista de compras:')
            for indice, item in enumerate(compras):
                print(indice, item)
        print('-' * 25)
    else:
        print('Opção inválida!')
        continue