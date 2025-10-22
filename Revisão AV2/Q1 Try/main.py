try:
    numeroUm = float(input("Digite o primeiro número (numerador): "))
    numeroDois = float(input("Digite o segundo número (divisor): "))
    
    resultadoDivisao = numeroUm / numeroDois
    print(f"Resultado da divisão: {resultadoDivisao}")

except ZeroDivisionError:
    print("Erro: O divisor não pode ser zero. Por favor, tente novamente.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas números.")
