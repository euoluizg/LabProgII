# Julia Cavalcante
# Luiz Gustavo
# Turma A

# 1 
numero = int(input("digite um numero:"))
for i in range(1, numero):
    print(f"{i} * 2 = {i * 2}")

# 2
produtos = [
{"nome": "Arroz", "preco": 5.49},
{"nome": "Feijão", "preco": 6.99},
{"nome": "Macarrão", "preco": 3.49},
{"nome": "Leite", "preco": 4.29},
{"nome": "Café", "preco": 8.99},
{"nome": "Açúcar", "preco": 2.99},
{"nome": "Óleo", "preco": 7.25},
]

while True:
    print("menu")
    print("1 - buscar produto")
    print("2 - sair")

    opcao = int(input("Digite a opcao: "))

    print("Qual produto deseja buscar?")

    if opcao == 1:
        produto = input("Digite o nome do produto: ")

        # if any(p["nome"] == produto for p in produtos):
        #     print(produtos)
        for i in produtos:
            if i == produto:
                print("oi")
    elif opcao == 2:
        print("saindo...")
        break
    else:
        print("invalido")


# 3
notaFiscal = []

while True:
    produto = input("Digite o nome do produto: ")
    preco = input("Digite o preço: ")
    dataCompra = input("Digite a data de compra: ")

    notaFiscal.append({'produto': produto, 'preco': preco, 'dataCompra': dataCompra})

    print(f"{notaFiscal}")
    break

