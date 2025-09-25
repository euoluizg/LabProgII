def verificarPar(numero):
    if numero % 2 == 0:
        return True
    elif numero % 2 != 0:
        return False
    else:
        return verificarPar(numero)