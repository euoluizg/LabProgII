def qtdPalavra(frase, palavra):
    frase_minuscula = frase.lower()
    palavra_minuscula = palavra.lower()
    palavras_frase = frase_minuscula.split()
    quantidade = 0
    for p in palavras_frase:
        if p == palavra_minuscula:
            quantidade += 1
    return quantidade