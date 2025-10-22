def dividir(numeroA, numeroB):
    try:
        resultado = numeroA / numeroB
        return resultado
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    except TypeError:
        return "Erro: Ambos os parâmetros devem ser números."
