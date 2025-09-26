# Questão 1 - Manipulação de listas e strings

import qtdPalavra

frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

quantidade = qtdPalavra.qtdPalavra(frase, palavra)

print(f"A palavra '{palavra}' aparece {quantidade} vezes na frase.")