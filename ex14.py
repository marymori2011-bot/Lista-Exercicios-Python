numeros = []

for i in range(8):
    numeros.append(int(input(f"Número {i+1}: ")))


maior = numeros[0]
menor = numeros[0]


for num in numeros:

    if num > maior:
        maior = num

    if num < menor:
        menor = num


print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
