produtos = []

def cadastro_de_itens(quantidade):
    for i in range(quantidade):
        novo_item = {"item": input('Digite o nome do item: '), "preco": float(input("Digite o valor do produto: "))}

        produtos.append(novo_item)   

    print(produtos)
    

quantidade = int(input("Digite a quantidade de itens a serem cadastrados: "))
cadastro_de_itens(quantidade)
