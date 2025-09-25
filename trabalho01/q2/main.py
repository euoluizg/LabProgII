# Q2 - Conversor de Temperatura
# Conversão entre Celsius e Fahrenheit
# Obrigração: criar um arquivo conversor.py e importar as funções

from conversor import conversorFahrenheit, conversorCelsius

print("Conversor de Temperatura")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
opcao = int(input("Escolha uma opção (1 ou 2): "))

if opcao == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = conversorFahrenheit(celsius)
    print(f"{celsius}°C é igual a {resultado:.2f}°F")

elif opcao == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = conversorCelsius(fahrenheit)
    print(f"{fahrenheit}°F é igual a {resultado:.2f}°C")
else:
    print("Opção inválida.")