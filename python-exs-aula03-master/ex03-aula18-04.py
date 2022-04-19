idade, maiores, media, somam, ridade = [], 0, 0, 0, 1
print('Entrada:')
for i in range(10):
    while ridade > 0:
        try:
            ridade = int(input(f"Digite a idade do {i+1}° aluno: "))
            break
        except:
            print("O valor digitado não é válido!")
    idade.append(ridade)
    if ridade > 15:
        maiores += 1
    else:
        media += 1
        somam += ridade
print(f'\nSaída:\nA quantidade de alunos que podem votar é {maiores}')
print(f'A méidia da idade dos alunos não eleitores é {(somam/media):.2f}')