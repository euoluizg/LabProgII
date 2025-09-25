def real_para_dolar(real, cotacao):
    return real / cotacao

def dolar_para_real(dolar, cotacao):
    return dolar * cotacao

def converter(valor, cotacao, tipo="real_para_dolar"):
    if tipo == "real_para_dolar":
        return real_para_dolar(valor, cotacao)
    elif tipo == "dolar_para_real":
        return dolar_para_real(valor, cotacao)
    else:
        raise ValueError("Tipo de conversão inválido. Use 'real_para_dolar' ou 'dolar_para_real'.")