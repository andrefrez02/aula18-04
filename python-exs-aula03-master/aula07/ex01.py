print('Entrada:\nFaça um programa em Python que imprima os números pares entre 0 e 100.\n')
print('Saída: ')
for i in range(101):
    x = i % 2
    if x == 0:
        if i == 0:
            pass
        elif i < 10:
            print('', i, end = ', ')
        elif i == 100:
            print(i, end = '.')
        elif str(i) in '102030405060708090':
            print(i, end = ', \n')
        else:
            print(i, end = ', ')