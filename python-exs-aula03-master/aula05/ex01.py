'''Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
▪ não-eleitor (abaixo de 16 anos)
▪ eleitor obrigatório (entre 18 e 65 anos)
▪ eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)'''
idade = int(input(f'Entrada:\nDigite o valor da sua idade: '))
print('\nSaída:')
if idade < 16:
    print('Você ainda não tem idade para ser eleitor.')
elif idade >= 16 and idade < 18:
    print('Você pode votar, mas não é obrigatório ainda.')
elif idade >= 18 and idade < 65:
    print('Você é obrigado a ir votar')
else:
    print('Você pode votar, mas não é obrigatório mais.')