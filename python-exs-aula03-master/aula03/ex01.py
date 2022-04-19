h = float(input('Entrada:\nDigite o valor da altura do tronco da pirâmide: '))
Bmenor = float(input('Digite o valor da base menor do tronco da pirâmide: '))
Bmaior = float(input('Digite o valor da base maior do tronco da pirâmide: '))

volume = h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)

print(f'\nSaída:\nO volume da pirâmide é de: {volume:.2f}')