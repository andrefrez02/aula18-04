'''3- Faça um programa em Python que obtenha o valor de uma compra, calcular e
mostrar o valor da compra considerando o desconto, conforme descrito abaixo:
• para compras acima de R$ 200 a loja dá um desconto de 20%
• para as abaixo disso não tem desconto, mostre o valor da compra.'''
compra = float(input('Entrada:\nDigite o valor da sua compra: R$'))

print('\nSaída: ')
if compra > 200:
    compra = compra - (compra * 0.20)
    print(f'O valor da sua compra com desconto é de: R${compra:.2f}')
else:
    print(f'O valor da sua compra é de: R${compra:.2f} - Você não obteve o desconto! :c')