# Luiz Gustavo de Melo Silva
# Teofanes Ferreira Albuquerque Junior


print("1")
print("") 
listaAlunos = []

aluno1 = input("Digite o nome do aluno 1: ")
aluno2 = input("Digite o nome do aluno 2: ")

listaAlunos.append(aluno1)
listaAlunos.append(aluno2)

try:
    indice = int(input("Digite o índice do aluno que deseja acessar: "))
    print(f"Aluno no índice {indice}: {listaAlunos[indice - 1]}")
except IndexError:
    print("Erro: Índice fora do intervalo. Por favor, insira 1 ou 2.")

print("")
print("-----")
print("")

print("2")
print("")

def validarEmail(email):
    if len(email) < 8:
        return "Erro: O email deve ter pelo menos 8 caracteres."
    elif "@" not in email:
        return "Erro: O email deve conter o caractere '@'."
    else:
        return "Email válido."
    
emailInput = input("Digite um email para validação: ")
resultadoValidacao = validarEmail(emailInput)
print(resultadoValidacao)

print("")
print("-----")
print("")

print("3")
print("")
def calcular_preco_ingresso(idade, estudante):
    if idade < 12:
        return 10.00
    elif 12 <= idade <= 17:
        return 15.00
    else:
        if estudante:
            return 20.00
        else:
            return 30.00



resultado = calcular_preco_ingresso(18, True)
print(f"Você pagará {resultado} reais")

print("")
print("-----")
print("")

print("4")
print("")
def calcular_idade(ano_nascimento, ano_atual):
    idade = ano_atual - ano_nascimento
    return idade


ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = calcular_idade(ano_nascimento, ano_atual)
print(f"A idade da pessoa é: {idade} anos")