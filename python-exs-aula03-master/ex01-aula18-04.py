resp, c = 'n', 0
print('Entrada: ')
while not resp in 'Ss':
    resp = input('Já dormi s/n?: ')
    c += 1
print(f'\nSaída:\nVocê contou {c} carneirinhos!')