print('Entrada:\nFaça um programa em Python que leia um valor n, inteiro e positivo, calcule e',
      'mostre a seguinte soma: ',
      'S = 1 + 1/2 + 1/3 + 1/4 +...+ 1/n\n')
n = float(input('Digite um valor inteiro e positivo: '))
n = str(n)
intCheck = n.rsplit('.')

if not intCheck[0] >= '1':
    intCheck[1] = '1'
while intCheck[1] != '0':
    n = float(input('O valor deve ser inteiro e positivo!\nDigite novamente um valor inteiro e positivo: '))
    n = str(n)
    intCheck = n.rsplit('.')

n = int(intCheck[0])
c = 0
for i in range(n):
    c += 1
    if n == 1:
        print('S = 1')
    elif c == 1:
        res = 1
        print(f'S = {c}', end = ' +')
    elif c == n:
        res = res + 1/c
        print(f' 1/{c}\nS = {res:.2f}')
    else:
        res = res + 1/c
        print(f' 1/{c}', end = ' +')