# Exercício 15 - Lista de Presença
# Conceitos: Listas, while/for, Condicionais, Contadores

alunos = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']
nome_busca = input('Nome a buscar: ')
encontrado = False

# Percorrendo a lista manualmente sem usar o operador 'in'
for aluno in alunos:
    if aluno == nome_busca:
        encontrado = True

if encontrado:
    print('Aluno encontrado!')
else:
    print('Aluno não está na lista.')
