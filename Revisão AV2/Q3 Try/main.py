def gerarETratarErros(entradaA, entradaB):
    try:
        a = float(entradaA)
        b = float(entradaB)
        resultado = a / b
        print(f"Resultado da operação: {resultado}")
        
    except ValueError:
        print("Tratamento de Erro: Ocorreu um ValueError. Certifique-se de que ambas as entradas são números.")
    except ZeroDivisionError:
        print("Tratamento de Erro: Ocorreu um ZeroDivisionError. O segundo número (divisor) não pode ser zero.")
    # ...
