import random

print("----------Lista-Exercicio----------")
print("")

# 1 - Faça um programa que peça um número interio e determine se ele é par ou ímpar. Dica: utilize o 
# operador módulo (resto da divisão[%]).

num = int(input("Digite um número: "))

if (num % 2 == 0):
    print(f"O {num} é par.")
else:
    print(f"O {num} é ímpar.")

print("")
print("-----------------------------------")
print("")

# 2 - Faça um programa que peça 2 números e imprima o maior deles.

num1 = int(input("Digite um número: "))

num2 = int(input("Digite outro número: "))

if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
elif num1 < num2:
    (print(f"O número {num2} é maior que o número {num1}."))
else:
    print("Os números são iguais.")

print("")
print("-----------------------------------")
print("")

# 3 - Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

vogal = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if letra in vogal:
    print(f"A letra '{letra}' é uma vogal.")
else:
    print(f"A letra '{letra}' é uma consoante.")

print("")
print("-----------------------------------")
print("")

# 4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a 
# média alcançada por aluno e apresentar:
#   a - A mensagem "Aprovado", se a média alcançada for menor do que sete;
#   b - A mensagem "Reprovado", se a média for menor do que sete;
#   c - A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    print(f"O Aluno está APROVADO COM DISTINÇÃO com média {media}.")
elif media >= 7:
    print(f"O Aluno está APROVADO com média {media}.")
else:
    print(f"O Aluno está REPROVADO com média {media}.")

print("")
print("-----------------------------------")
print("")

# 5 - Faça um programa que leia 3 números e mostre o maior deles.

num3 = int(input("Digite um número: "))
num4 = int(input("Digite um segundo número: "))
num5 = int(input("Digite um terceiro número: "))

if num3 >= num4 and num3 >=num5:
    maior = num3
elif num4 >= num3 and num4 >=num5:
    maior = num4
else:
    maior = num5
    
print(f"O maior número entre {num3}, {num4} e {num5}, é {maior}")

print("")
print("-----------------------------------")
print("")

# 6 - Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino 
# ou N-noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = input("Digite o turno que você estuda: ")

matutino = ['m', 'M', 'matutino', 'Matutino', 'Matutino']

vespertino = ['v', 'V', 'vespertino', 'Vespertino', 'VESPERTINO']

noturno = ['n', 'N', 'noturno', 'Noturno', 'Noturno']

if turno in matutino:
    print("Bom Dia!")
elif turno in vespertino:
    print("Boa Tarde!")
elif turno in noturno:
    print("Boa Noite!")
else:
    print("Turno Inválido!")

print("")
print("-----------------------------------")
print("")

# 7 - Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#   a - "Telefonou para a vítima?"
#   b - "Esteve no local do crime?"
#   c - "Mora perto da vítima?"
#   d - "Devia para a vítima?"
#   e - "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classficação sobre a participação da pessoa no crime. Se a pessoa 
# responder positivamente a 2 questÕes ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
# 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

perguntasRandom = random.sample(perguntas, len(perguntas))

respostasPositivas = 0

for pergunta in perguntasRandom:
    resposta = input(f"{pergunta} (S/N): ").strip().lower()
    if resposta == 's' or resposta == 'sim':
        respostasPositivas += 1

if respostasPositivas == 2:
    classification = "Suspeito"
elif 3 <= respostasPositivas <= 4:
    classification = "Cúmplice"
elif respostasPositivas == 5:
    classification = "Assassino"
else:
    classification = "Inocente"

print(f"\n Classificação: {classification}")