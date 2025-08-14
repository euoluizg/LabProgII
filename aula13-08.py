contador = 1
notas = []

while contador <= 3:
    nota = float(input(f"Digite a nota {contador}: "))
    notas.append(nota)
    contador += 1

print(notas)