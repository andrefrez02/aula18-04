'''Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de
segundo grau, apresentando: 
as duas raízes, quando for possível efetuar o cálculo(delta positivo ou zero);
a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta negativo);
e a mensagem "Não é equação do segundo grau", se o valor de a for igual a zero.'''
a = float(input('Entrada:\nDigite o coeficiente A: '))
while a == 0:
    print('\nO valor de A não pode ser igual a 0.')
    a = float(input('Digite o coeficiente A novamente: '))

b = float(input('Digite o coeficiente B: '))
c = float(input('Digite o coeficiente C: '))

delta = b*b - 4*a*c
print('\nSaída:')

if delta < 0:
    print('Não há raízes reais(delta negativo).')
else: 
    x1 = (-b + delta**0.5) / 2*a
    x2 = (-b - delta**0.5) / 2*a
    print(f'As raízes são:\nx1 = {x1:.2f} e x2 = {x2:.2f}')