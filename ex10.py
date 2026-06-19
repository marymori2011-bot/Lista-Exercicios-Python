def calcular_fatorial(n):
    fat = 1

    for i in range(1, n + 1):
        fat = fat * i

    return fat


n = int(input("Digite um número: "))

resultado = calcular_fatorial(n)

print(f"{n}! = {resultado}")
