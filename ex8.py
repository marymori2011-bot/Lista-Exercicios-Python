soma = 0

numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma = soma + numero
    numero = int(input("Digite outro número: "))

print(f"Soma: {soma}")
