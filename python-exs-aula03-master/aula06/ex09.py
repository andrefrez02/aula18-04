'''Faça um programa que solicite dois números reais e execute as operações
listadas a seguir de acordo com a escolha do usuário:
Escolha do usuário Operação
1 Média entre os números digitados
2 Diferença entre o maior e o menor número digitado
3 Produto entre os números digitados
4 Divisão do primeiro pelo segundo
▪ Se a opção digitada for inválida,
mostrar mensagem de erro.
▪ Na operação 4, o segundo
número não pode ser zero.'''
val1 = float(input('Entrada:\nDigite o valor de A: '))
val2 = float(input('Digite o valor de B: '))
op = input('Digite qual operação vai ser feita["1" - Média, "2" - Diferença maior-menor, "3" - Produto e "4" - Divisão n1/n2]: ')
while op not in '1234':
    op = input('\nA opção digitada é inválida.\nDigite novamente qual operação vai ser feita["1" - Média, "2" - Diferença maior-menor, "3" - Produto e "4" - Divisão n1/n2]: ')

match op:
    case '1':
        res = [(val1 + val2 / 2), 'média', '+', '/ 2']
    case '2':
        res = [(val1 - val2), 'diferença', '-', '\b']
    case '3':
        res = [(val1 * val2), 'produto', '*', '\b']
    case '4':
        while val2 == 0:
            val2 = float(input('Impossível dividir por 0!\nDigite novamente o valor de B: '))
        res = [(val1 / val2), 'divisão', '/', '\b']

if op == '1':
    print(f'\nSaída\nO resultado da operação de {res[1]} dos valores: [A: {val1}, B: {val2}]\nÉ igual a: ({val1} {res[2]} {val2}) {res[3]} = {res[0]:.2f}')
else:
    print(f'\nSaída\nO resultado da operação de {res[1]} dos valores: [A: {val1}, B: {val2}]\nÉ igual a: {val1} {res[2]} {val2} {res[3]} = {res[0]:.2f}')