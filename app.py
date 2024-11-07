


#Definição da lista de dicionarios que contem o nome do item e seu devido valor

produtos = [

    {"item": "maça", "preco": 2.0},
    {"item": "banana", "preco": 4},
    {"item": "pera", "preco": 3},
    {"item": "melancia", "preco": 8},
    {"item": "morango", "preco": 1}

]


nome_user = (input("Digite o nome de usuario: "))



def inicio():
    
    quantidade_de_itens = int(input(f"Olá {nome_user} como vai você ? \nQual a quantidade de itens comprados? "))
    
    for i in range(quantidade_de_itens):
        item = input(f"Digite o {i + 1}º item: ").lower()
        compras_user.append(item)
    calculo(compras_user)



compras_user = []

def calculo(compras_user):

    valor_total = 0
    
    for item in compras_user:
        for produto in produtos:
            if produto["item"] == item:
                valor_total += produto["preco"]
                break    
   
        
    print(f"O valor total da compra de {nome_user} corresponde a {valor_total}")

       
       










inicio()






















