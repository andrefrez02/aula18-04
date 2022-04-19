'''Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
Valor de compra                     Valor de venda
valor < R$10,00                      lucro de 70%
R$ 10,00 <= valor < R$ 30,00         lucro de 50%
R$ 30,00 <= valor < R$ 50,00         lucro de 40%
valor >= R$50,00                     lucro de 30%
Crie uma programa que permita digitar o nome do produto e valor da compra, e
imprimindo o nome do produto e o valor da venda.
'''
produtos, valores, lucros, resp = [], [], [], 'x'
print('Entrada:')
while resp not in 'Ss': 
    nome_produto = str(input('Digite o nome do produto: '))
    produtos.append(nome_produto)
    valor_compra = float(input('Digite o valor de compra desse produto: R$'))
    valores.append(valor_compra)
    resp = input('Digite "S" para sair ou "N" para continuar inserindo produtos: ')
    print('')
    if valor_compra < 10:
        valor_venda = (0.7 * valor_compra) + valor_compra
    elif valor_compra > 10 and valor_compra < 30:
        valor_venda = (0.5 * valor_compra) + valor_compra
    elif valor_compra > 30 and valor_compra < 50:
        valor_venda = (0.4 * valor_compra) + valor_compra
    else:
        valor_venda = (0.3 * valor_compra) + valor_compra
    lucros.append(valor_venda)
    while resp not in 'SsNn':
        resp = input(f'O valor "{resp}" está incorreto, digite "S" para sair ou "N" para continuar inserindo produtos: ')

if resp in 'Ss':
    count = 0
    print('Saída:')
    for i in produtos:
        print(f'{count + 1}º produto:\nNome do produto: {produtos[count]} | Valor de compra: {valores[count]:.2f} | Valor de venda: {lucros[count]:.2f} |')
        count += 1