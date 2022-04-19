tam = int(input('Entrada:\nDigite o tamanho do arquivo em MB: '))
vel = int(input('Digite a velocidade do link de internet(Mbps): '))
temp = tam / vel
segundos = temp % 60
minutos = temp // 60

print(f'\nSaída:\nTempo aproximado para download: {minutos:.2f} minutos e {segundos:.2f} segundos')