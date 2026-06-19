# Exercício 16 - Ordenação Bolha (Bubble Sort)
# Conceitos: Listas, Laços aninhados, Troca de valores

numeros = []
for i in range(6):
    numeros.append(int(input(f'Número {i+1}: ')))

n = len(numeros)

# Implementação do Bubble Sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numeros[j] > numeros[j + 1]:
            # Troca de elementos em uma única linha (recurso nativo do Python)
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print('Lista ordenada:', numeros)
