# Questão 4 - Verificador de Números Pares e Ímpares
# Crie uma função que receba um número inteiro e retorne se ele é par ou ímpar.

from verificador import verificarPar

numero = int(input("Digite um número: "))

if verificarPar(numero):
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")