print("------------Revisão-AV1------------")
print("")

# 1 - Crie um programa em Python que leia um valor inteiro e exivba todos os números
# pares e ímpares no intervalo de 1 a esse valor.

numInteiro = int(input("Digite um número inteiro: "))
print("")

if numInteiro < 1:
    print("Por favor, digite um número maior ou igual a 1: ")
else:
    print(f"Números pares de 1 até {numInteiro}:")
    for nI in range(1, numInteiro + 1):
        if nI % 2 == 0:
            print(nI, end=" ")

    print("")

    print(f"Números ímpares de 1 até {numInteiro}")
    for nI in range(1, numInteiro + 1):
        if nI % 2 != 0:
            print(nI, end=" ")

print("")
print("-----------------------------------")
print("")

# 2 - Desenvolva um algoritmo em Python que receba 3 notas e faça a média. O sistema deverá exibir:
# - Aprovado: se a média for maior ou igual a 7;
# - Reposição: se a média for menor que 7 mas maior ou igual a 4;
# - Reprovado: se a média for menor que 4

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print("")

if media >= 7:
    print(f"Aprovado! Com média {media}")
elif media >= 4:
    print(f"Reposição! Com média {media}")
else:
    print(f"Reprovado! Com média {media}")

print("")
print("-----------------------------------")
print("")

# 3 - Escreva um programa em Python que solicite ao usúario um valor inteiro (denomindao como 'n').
# O programa deve exibir o dobro desse valor para todos os números de 1 até 'n', ou seja, para cada
# número no intervalo de 1 até 'n', você deverá calcular e mostrar o dobro desse número.

n = int(input("Digite um número: "))

if n < 1:
    print("Por favor, digite um número maior ou igual a 1.")
else:
    print(f"O dobro dos números de 1 até {n}")
    for num in range(1, n + 1):
        dobro = num * 2
        print(f"O dobro do {num} é {dobro}")


print("")
print("-----------------------------------")
print("")

# 4 - Você foi designado para desenvolver um programa que converta temperaturas entre diferentes escalas.
# Suas tarefas são as seguintes:
# a) Escreva um programa em Python que exiba um menu com as seguintes opções:
# 1 - Converter de Celsius para Fahrenheit
# 2 - Converter de Fahrenheit para Celsius
# 3 - Sair
# b) Caso usúario selciona 1 (converter Celsius para Fahrenheit)
# Realize a conversão da temperatura de Celsisus para Fahrenheit utilizando a fórmula: 
# Fahrenheit = (Celsius* 9/5) + 32. Exiba ao resultado da conversão
# c) Caso usúario selecione 2 (converter Fahrenheit para Celsius)
# Realize a conversão da temperatura de Fahrenheit para Celsius utilizando a fórmula: 
# Celsius = (Fahrenheit - 32) * 5/9. Exiba o resultado da conversão
# d) Caso usúario selecione 3 (Sair)

while True:
    print("-----------Menu-Conversor----------")
    print("")
    print("1 - Converter de Celsius para Fahrenheit")
    print("2 - Converter de Fahrenheit para Celsius")
    print("3 - Sair")

    option = int(input("Digite uma opção (1, 2 ou 3): "))

    if option == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Resultado: {fahrenheit:.1f}°F")
    elif option == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Resultado: {celsius: .1f}˚C")
    elif option == 3:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")

print("")
print("-----------------------------------")
print("")

# 5 - Crie uma lista contendo dicionários de produtos de forma a representar:
#  [{
#       'nome': 'Nome do Produto 1'
#       'preco': 'Preço do Produto 1'
#  },
#  {
#       'nome': 'Nome do Produto 2'
#       'preco': 'Preço do Produto 2'
# }]
# Motre ao usúario todos os produtos desta lista, respeitando a seguinte saída:
# Produto 1 - 50 R$
# Produto 2 - 60 R$
# ...
# Produto N - xx R$

produtos = [
    {'nome': 'Notebook', 'preco': 3500},
    {'nome': 'Mouse Gamer', 'preco': 120},
    {'nome': 'Teclado Mecânico', 'preco': 280},
    {'nome': 'Monitor 24"', 'preco': 900},
    {'nome': 'Headset', 'preco': 150}
]

for produto in produtos:
    print(f"{produto['nome']} - {produto['preco']} R$")