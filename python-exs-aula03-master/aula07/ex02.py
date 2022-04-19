print('Entrada:\nFaça um programa em Python que imprima os números de 1 a 50 de 1 em 1',
     'e de 52 a 100 de 2 em 2.\n')
print('Saída: ')
for i in range(51):
    if i == 0:
        pass
    elif i < 10:
        print('', i, end = ', ')
    elif i == 50:
        print(i, end = ',\n')
    elif str(i) in '10203040':
        print(i, end = ', \n')
    else:
        print(i, end = ', ')
for i in range(52, 102, 2):
    if str(i) in '7090':
        print(i, end = ', \n')
    elif i == 100:
        print(i, end = '.')
    else:
        print(i, end = ', ')