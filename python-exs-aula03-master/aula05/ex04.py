'''Elabore um programa em Python que implemente uma calculadora com as funções
de somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
valores, e perguntar qual a operação pretendida (‘+’, ‘-‘, ‘*’ ou ‘/’ ) e a seguir calcular e 
mostrar o resultado'''
val1 = float(input('Entrada:\nDigite o valor de A: '))
val2 = float(input('Digite o valor de B: '))
op = input('Digite qual operação vai ser feita["1" - Soma, "2" - Subtração, "3" - Multiplicação e "4" - Divisão]: ')
while op not in '1234':
    op = input('\nA opção digitada é inválida.\nDigite novamente qual operação vai ser feita["1" - Soma, "2" - Subtração, "3" - Multiplicação e "4" - Divisão]: ')

match op:
    case '1':
        res = [(val1 + val2), 'soma', '+']
    case '2':
        res = [(val1 - val2), 'subtração', '-']
    case '3':
        res = [(val1 * val2), 'multiplicação', '*']
    case '4':
        res = [(val1 / val2), 'divisão', '/']

print(f'\nSaída\nO resultado da operação de {res[1]} dos valores: [A: {val1}, B: {val2}]\nÉ igual a: {val1} {res[2]} {val2} = {res[0]:.2f}')