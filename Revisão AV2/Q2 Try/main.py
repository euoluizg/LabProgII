try:
    entradaUsuario = input("Digite um número: ")
    numeroConvertido = float(entradaUsuario)
    print(f"Número digitado (convertido para float): {numeroConvertido}")
except ValueError:
    print("Erro: O que você digitou não é um número válido. Por favor, digite apenas números.")
