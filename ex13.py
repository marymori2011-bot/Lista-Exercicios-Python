def calcular_soma(lista):
    total = 0

    for numero in lista:
        total += numero

    return total


numeros = []

for i in range(5):
    n = float(input(f"Número {i+1}: "))
    numeros.append(n)


soma = calcular_soma(numeros)

media = soma / len(numeros)

print(f"Soma: {soma}")
print(f"Média: {media:.2f}")
