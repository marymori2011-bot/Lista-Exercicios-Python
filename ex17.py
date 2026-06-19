# Exercício 17 - Função que Retorna Lista
# Conceitos: Funções, Listas, for, return

def somente_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

# Programa Principal
numeros = []
for i in range(10):
    numeros.append(int(input(f'Número {i+1}: ')))

resultado = somente_pares(numeros)
print('Números pares:', resultado)
