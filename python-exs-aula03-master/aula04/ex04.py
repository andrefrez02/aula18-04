'''Escreva um programa em Python que solicite ao usuário os valores de três
contas de consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique
se o salário é suficiente para pagar as três contas, caso não seja apresente a
mensagem “Salário insuficiente!”. Caso seja, apresente o valor que restou do
salário após pagar as contas.'''
conta1 = float(input('Entrada:\nDigite o valor da sua conta de água: R$'))
conta2 = float(input('Digite o valor da sua conta de luz: R$'))
conta3 = float(input('Digite o valor da sua conta de internet: R$'))
sal = float(input('Digite o valor do seu salário: R$'))

conta = conta1 + conta2 + conta3
print(f'Saída:\nValor total das contas: R${conta}')
if sal < conta:
    print(f'Seu salário é insuficiente para pagar as contas!\nVocê deveria ganhar no mínimo mais R${conta - sal} para conseguir pagar as suas contas...')
else:
    print(f'Seu salário é suficiente para pagar as contas!\nApós pagá-las te restará ainda R${sal - conta}')