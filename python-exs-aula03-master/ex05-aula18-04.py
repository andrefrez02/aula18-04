soma = 0
turmas = int(input('Entrada:\nDigite a quantidade de turmas: '))
for i in range(turmas):
    qnt = int(input(f'Digite a quantidade de alunos da {i + 1}ª turma: '))
    soma += qnt
print(f'\nSaída:\nAs turmas têm em média {soma/turmas:.0f} alunos.')