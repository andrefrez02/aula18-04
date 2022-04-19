soma = 0
conta = input('Digite o número da conta com 04 digítos: ')

for i in conta:
    soma  = soma + int(i)
dig = soma%10

print(f'Número da conta: 00{conta}-{dig}')