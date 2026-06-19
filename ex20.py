# Exercício 20 - Relatório de Turma
# Conceitos: Listas, Funções múltiplas, for, Condicionais, Estatísticas

def calcular_media(lista_notas):
    return sum(lista_notas) / len(lista_notas)

def contar_aprovados(lista_notas):
    aprovados = 0
    for nota in lista_notas:
        if nota >= 6.0:
            aprovados += 1
    return aprovados

def melhor_aluno(lista_nomes, lista_notas):
    maior_nota = lista_notas[0]
    nome_melhor = lista_nomes[0]
    
    for i in range(1, len(lista_notas)):
        if lista_notas[i] > maior_nota:
            maior_nota = lista_notas[i]
            nome_melhor = lista_nomes[i]
            
    return nome_melhor

# Programa Principal
nomes = []
notas = []

for i in range(5):
    nomes.append(input(f'Nome do aluno {i+1}: '))
    notas.append(float(input(f'Nota do aluno {i+1}: ')))

# Saída do Relatório Completo
print('\n=== RELATÓRIO DA TURMA ===')
for i in range(5):
    print(f'Aluno: {nomes[i]:10} | Nota: {notas[i]:.1f}')
print('-' * 30)
print(f'Média da Turma:          {calcular_media(notas):.2f}')
print(f'Quantidade de Aprovados: {contar_aprovados(notas)}')
print(f'Melhor Aluno da Turma:   {melhor_aluno(nomes, notas)}')
