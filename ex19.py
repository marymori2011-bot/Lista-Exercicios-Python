# Exercício 19 - Sequência de Fibonacci com Lista
# Conceitos: Listas, Funções, for, Variáveis

def gerar_fibonacci(n):
    fib = []
    if n >= 1:
        fib.append(0)
    if n >= 2:
        fib.append(1)
    
    for i in range(2, n):
        proximo = fib[i - 1] + fib[i - 2]
        fib.append(proximo)
    return fib

# Programa Principal
n = int(input('Quantos termos? '))
sequencia = gerar_fibonacci(n)
print('Fibonacci:', sequencia)
