# Exercício 18 - Contagem de Vogais
# Conceitos: Variáveis, String, for, Condicionais, Contadores

frase = input('Digite uma frase: ')
contador = 0
vogais = 'aeiouAEIOU'

# Iteração direta sobre os caracteres da string
for letra in frase:
    if letra in vogais:
        contador += 1

print(f'Total de vogais: {contador}')
