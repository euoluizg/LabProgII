def verificarAcao(precoAcao):
    limitePreco = 150.99
    if precoAcao > limitePreco:
        return "Ação está cara! Compre com cuidado."
    else:
        return "Ação está barato!"
