print("----------Lista-Exercicio----------")
print("")

# 1 - Faça um programa, utilizando while, que mostre na tela os números de 0 a 100.

num = 0 

print("Números de 0 a 100:")
while num <= 10:
    print(num)
    num += 1

print("")
print("-----------------------------------")
print("")

# 2 - Faça um programa, utilizando while, que mostre na tela de o até N, em que N é o limite inserido pelo usuário.

num1 = int(input("Digite um número limite: "))
cont = 0

while cont <= num1:
    print(cont)
    cont += 1

print("")
print("-----------------------------------")
print("")

# 3 - Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.

continuar = "s"

while continuar == "s":
    num2 = float(input("Digite o primeiro número: "))
    num3 = float(input("Digite o segundo número: "))

    soma = num2 + num3
    print(f"A soma de {num2} + {num3} = {soma}")

    continuar = input("Deseja fazer outra soma? (s/n): ").strip().lower()

print("")
print("-----------------------------------")
print("")
print("--------------Desafio--------------")
print("")

# 1 - A série de Fibonacci é formada pela sequência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55... Faça um programa que 
# gere a serie até que o valor seja maior que 500.

atual = 0
proximo = 1

while atual <= 500:
    print(atual, end=", ")
    atual, proximo = proximo, atual + proximo


print("")
print("-----------------------------------")
print("")

# 2 - Faça o programa que, dado um conjuto de N números, determine o menor valor, o maior valor e a soma dos valores.

totalNum = int(input("Quantos números deseja digitar? "))

num4 = []  

for i in range(totalNum):
    num5 = float(input(f"Digite o {i+1}º número: "))
    num4.append(num5)

menor = min(num4)
maior = max(num4)
soma = sum(num4)

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")

print("")
print("-----------------------------------")
print("")

# 3 - Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

numTotal = int(input("Quantos números deseja digitar? "))

num6 = []  

for i in range(numTotal):
    while True:  # repete até receber um valor válido
        num7 = float(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
        if 0 <= num7 <= 1000:
            num6.append(num7)
            break
        else:
            print("Valor inválido! Digite um número entre 0 e 1000.")

menor = min(num6)
maior = max(num6)
soma = sum(num6)

print(f"\nMenor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")

print("")
print("-----------------------------------")
print("")

# 4 - Faça um programa que leia e valide as seguintes informações:
#       1. Nome: maior que 3 caracteres;
#       2. Idade: entre 0 e 150;
#       3. Salário: maior que zero;
#       4. Sexo: 'f' ou 'm''
#       5. Estado Civil: 's', 'c', 'v', 'd';
#       6. Use a função len(string) para saber o tamanho de um texto (número de caracteres).

nome = input("Digite seu nome: ")
while len(nome) <= 3:
    print("Erro: o nome deve ter mais que 3 caracteres.")
    nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Erro: a idade deve estar entre 0 e 150.")
    idade = int(input("Digite sua idade: "))

salario = float(input("Digite seu salário: "))
while salario <= 0:
    print("Erro: o salário deve ser maior que zero.")
    salario = float(input("Digite seu salário: "))

sexo = input("Digite seu sexo (f/m): ").lower()
while sexo not in ['f', 'm']:
    print("Erro: sexo deve ser 'f' ou 'm'.")
    sexo = input("Digite seu sexo (f/m): ").lower()

estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()
while estado_civil not in ['s', 'c', 'v', 'd']:
    print("Erro: estado civil deve ser 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Digite seu estado civil (s/c/v/d): ").lower()

print("\nInformações cadastradas com sucesso:")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")

print("")
print("-----------------------------------")
print("")

# 5 - Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um numero primo é aquele
# que é divisível somente por ele mesmo e por 1.

num8 = int(input("Digite um número inteiro: "))

if num8 <= 1:
    print(f"{num8} não é um número primo.")
else:
    primo = True
    for divisor in range(2, int(num8**0.5) + 1):
        if num8 % divisor == 0:
            primo = False
            break

    if primo:
        print(f"{num8} é um número primo.")
    else:
        print(f"{num8} não é um número primo.")