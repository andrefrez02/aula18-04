'''Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a
quantidade de horas trabalhadas, calcule e mostre o valor do salário. Considere os
valores de horas a seguir, de acordo com o turno de trabalho. Caso o turno seja
igual a ‘N’ (utilize um caractere para representar) o valor da hora trabalhada é R$
45,00, caso contrário é R$ 37,50'''
turno = str(input('Entrada:\nDigite o seu turno de trabalho(N = noturno, M = manhã, T = tarde): '))
while turno not in 'NnMmTt':
    turno = str(input(f'\nO valor: "{turno}" não é válido!\nDigite um valor válido do seu turno de trabalho(N = noturno, M = manhã, T = tarde): '))

horas = int(input('Digite a quantidade de horas trabalhadas: '))

if turno in 'Nn':
    din = horas * 45.00
elif turno in 'MmTt':
    din = horas * 37.50

print(f'O valor do seu salário é de: R${din:.2f}.')