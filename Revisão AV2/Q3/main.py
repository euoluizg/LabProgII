from funcoesBolsa import verificarAcao

valorAcao = float(input("Digite o valor da ação: "))
if valorAcao:
    resultadoValidacao = verificarAcao(valorAcao)
    print(resultadoValidacao)
else:
    print("Valor inválido!")