def calculoIMC(peso, altura):
    if altura <= 0:
        return "Altura inválida."
    imc = peso / (altura ** 2)
    return imc

def classificarIMC(imc):
    if imc is None:
        return "IMC inválido."
    if imc < 18.5:
        return "Abaixo do peso."
    elif 18.5 <= imc < 24.9:
        return "Peso normal."
    elif 25 <= imc < 29.9:
        return "Sobrepeso."
    else:
        return "Obesidade."
    
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calculoIMC(peso, altura)
classificacao = classificarIMC(imc)
print(f"Seu IMC é: {imc:.2f}. Classificação: {classificacao}")
