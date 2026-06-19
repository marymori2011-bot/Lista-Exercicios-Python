def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("0 - Sair")

opcao = int(input("Escolha: "))

if opcao != 0:
    a = float(input("Primeiro número: "))
    b = float(input("Segundo número: "))

    if opcao == 1:
        print(somar(a, b))

    elif opcao == 2:
        print(subtrair(a, b))

    elif opcao == 3:
        print(multiplicar(a, b))

    elif opcao == 4:
        if b != 0:
            print(dividir(a, b))
        else:
            print("Não é possível dividir por zero")
