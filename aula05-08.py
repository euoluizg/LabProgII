print("----------------Exercicio----------------")

# 1 - Dada a entrada de um número -> Verificar se número é positivo, negativo ou zero.

print("1 - Dada a entrada de um número -> Verificar se número é positivo, negativo ou zero.")

num = float(input("Digite um número: "))

if num < 0:
    print(f"O número digitado é negativo. {num: .2f}")
elif num > 0:
    print(f"O número digitado é positivo. {num: .2f}")
else:
    print("O número digitado é zero.")

print("-----------------------------------------")

# 2 - Calculadora simples dada a entrada de "-+", "-", "/", "*" -> Realize a operação para a entrada de 2 números.

print("2 - Calculadora simples dada a entrada de '+', '-', '/', '*' -> Realize a operação para a entrada de 2 números.")

operator = input("Digite um operador matemático ('+' para somar, '-' para subtrair, '/' para divisão, '*' para multiplicação): ")

num2 = float(input("Digite um número: "))

num3 = float(input("Digite um outro número: "))

mult = num2 * num3

sum = num2 + num3

sub = num2 - num3

div = num2 / num3

if operator == "*":
    print(f"A multiplicação de{num2: .2f} *{num3: .2f} ={mult: .2f}")

elif operator == "/":
    print(f"A divisão de{num2: .2f} /{num3: .2f} ={div: .2f}")

elif operator == "-":
    print(f"A subtração de{num2: .2f} -{num3: .2f} ={sub: .2f}")
    
elif operator == "+":
    print(f"A adição de{num2: .2f} +{num3: .2f} ={sum: .2f}")

else:
    print("Operador matemático inválido. Digite um desses operadores (+, -, *, /)")

print("-----------------------------------------")

# 3 - Login: Se o usuário digitar username = "admin" e password = "admin", exibir mensagem de "Bem Vindo ao admin".

print("3 - Login: Se o usuário digitar username = 'admin' e password = 'admin', exbir mensagem de 'Bem Vindo ao admin'.")

username = input("Digite seu username: ")

password = input("Digite sua password: ")

if username and password == "admin":
    print("Bem Vindo ao admin")
else:
    print("Logado com sucesso.")

print("-----------------------------------------")

# 4 - Verificar se a idade permite votar 
#   a. >= 18 -> Obrigatório 
#   b. >= 16 -> Opcional
#   c. <  Não pode votar

print("4 - Verificar se a idade permite votar")
print("   a. >= 18 -> Obrigatório")
print("   b. >= 16 -> Opcional")
print("   a. < 16 -> Não pode votar")

idade = int(input("Digite sua idade para ser feita a verificação de direito ao voto: "))

if idade >= 18:
    print(f"Você tem {idade} anos, voto obrigatório.")
elif idade >= 16:
    print(f"Você tem {idade} anos, voto opcional.")
else:
    print(f"Você tem {idade} anos, não pode votar.")


print("-----------------------------------------")