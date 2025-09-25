import random

# 1. Calculadora de Ano Bissexto
# Faça um Programa que peça um ano e informe se ele é bissexto ou não.

# Dica: Um ano é bissexto se for divisível por 4, mas não por 100, exceto se for 
# divisível por 400. Por exemplo, 2000 e 2400 são bissextos, mas 1800, 1900 e 2100 não são.

# anoAtual = int(input("Digite o ano: "))

# if (anoAtual % 4 == 0 and anoAtual % 100 != 0) or (anoAtual % 400 == 0):
#     print(f"O ano {anoAtual} é bissexto.")
# else:
#     print(f"O ano {anoAtual} não é bissexto ")

# 2. Jogo de Adivinhação
# Crie um programa onde o computador "pensa" em um número inteiro entre 0 e 10 e pede para o 
# usuário tentar adivinhar qual foi o número escolhido. O programa deverá escrever na tela se 
# o usuário venceu ou perdeu.
# Dica: Você pode usar a biblioteca 'random' para gerar um número aleatório.

# scrtNumber = random.randint(1, 10)

# while True:
#     tentativas = int(input("Tente advinhar o numero secreto: "))

#     if tentativas == scrtNumber:
#         print(f"Você acertou o número secreto {scrtNumber}")
#         break
#     elif tentativas < scrtNumber:
#         print("Tente um número maior.")
#     else:
#         print("Tente um número menor.")

# 3. Cálculo de Fatorial
# Desenvolva um programa que peça ao usuário um número inteiro não-negativo e calcule o seu fatorial. 
# O fatorial de um número n (representado por n!) é o produto de todos os inteiros positivos menores ou iguais a n.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120. O fatorial de 0 é 1.
# Saída Esperada:
# Digite um número para calcular o fatorial: 5
# O fatorial de 5 é: 120

# number1 = int(input("Digite um número para calcular o fatorial: "))


# 4. Verificador de Palíndromo
# Faça um programa que leia uma palavra e verifique se ela é um palíndromo. Um palíndromo é uma palavra 
# que se lê da mesma forma de trás para frente.
# Dica: Ignore diferenças entre maiúsculas e minúsculas. Exemplos de palíndromos: "arara", "ovo", "radar".

# Saída Esperada:
# Digite uma palavra: Arara
# A palavra Arara é um palíndromo.
# Digite uma palavra: Python
# A palavra Python não é um palíndromo.

# 5. Análise de Números em uma Lista
# Escreva um programa que leia 5 números inteiros do usuário, armazene-os em uma lista e, ao final, mostre:
# a. A soma de todos os números.
# b. A média dos números.
# c. O maior e o menor valor digitado.

# numbers = []

# for number in numbers:
#     number = int(input("Digite um número: "))


# 6. (Desafio) Cadastro Simples de Usuário
# Crie um programa que simule um cadastro. O programa deve solicitar e validar as seguintes informações, 
# repetindo a solicitação até que uma entrada válida seja fornecida (similar ao exercício de validação da sua lista ):

# a. Nome de usuário: Deve ter no mínimo 5 caracteres.
# b. Senha: Deve ter no mínimo 8 caracteres e não pode ser igual ao nome de usuário.
# Após a validação bem-sucedida de ambos, exiba uma mensagem de "Cadastro realizado com sucesso".

usuarios = [
    {
        'user': 'admin',
        'password': 'admin123'
    }
]

while True:

    print("\n----Menu-Login----")
    print("1 - Login")
    print("2 - Sign up")
    print("3 - Sair")
    print("------------------")

    option = int(input("Selecione a opção: "))

    if option == 1:

        user = input("Digite o seu usuario: ").lower()
        password = input("Digite sua senha: ").lower()

        encontrado = None
        for u in usuarios:
            if u['user'] == user and u['password'] == password:
                encontrado = u
                print("Logado com sucesso.")
                break
        if user == 'admin' and password == 'admin123':
            print("Bem vindo ADMIN.")

            while True:
                print("\n----Menu-ADMIN----")
                print("1 - Todos usuarios")
                print("2 - Deletar")
                print("3 - Sair")
                print("------------------")

                option = int(input("Selecione a opção: "))
                
                if option == 1:
                    print("Usuários-cadatrados")
                    for idx, usr in enumerate(usuarios, start=1):
                        print(f"{idx} - {usr['user']}")
                elif option == 2:
                    print("Deletar-Usuários")
                    print("")
                    remover = input("Digite o usuário que deseja remover: ")

                    if remover == 'admin':
                        print("O usuário admin não pode ser removido")
                    else:
                        removido = False
                        for r in usuarios:
                            if r['user'] == remover:
                                usuarios.remove(r)
                                print(f"Usuário {r['user']} removido.")
                                removido = True
                                break
                elif option == 3:
                    print("Saindo do painel admin.")
                    break
                else:
                    print("Invalido.")
    elif option == 2:
        while True:
            user = input("Digite o seu usuario: ").lower()
            password = input("Digite sua senha: ").lower()
                
            if any(u['user'] == user for u in usuarios):
                print("Já existe um usuário com mesmo nome.")
            elif len(user) < 5:
                print("Usuário não tem caracteres minimos.(5)")
            elif len(password) < 8:
                print("Senha não tem caracteres minimos.(8)")
            elif user == password:
                print("Usuário e senha não podem ser iguais.")
            else:
                usuarios.append({'user': user, 'password': password})
                print("cadastrado.")
                break
    elif option == 3:
        print("Saindo.")
        break
    else:
        print("Invalido.")

