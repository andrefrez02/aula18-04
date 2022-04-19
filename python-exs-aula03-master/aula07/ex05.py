print('Temos um grupo de pessoas. Escreva um programa em Python que leia o',
'sexo e a altura de cada pessoa, calcule e mostre a altura média das mulheres e',
'dos homens separadamente. Utilize o comando de repetição que desejar.\n\nEntrada:')
cadastros_sexo, cadastros_altura = [], []
resp, count, count_homem, count_mulher = 's', 0, 0, 0
rsexo, raltura = 'n', 0
while not resp in 'nN':
    while not rsexo in 'FfMm':
        rsexo = input('Digite o sexo dessa pessoa[F/M]: ')
        cadastros_sexo.append(rsexo)
        if rsexo in 'fF':
            count_mulher += 1
        elif rsexo in 'mM':
            count_homem += 1
    while raltura :
        raltura = float(input('Digite a altura dessa pessoa em m: '))
        cadastros_altura.append(raltura)
    count += 1
    rsexo = 'x'
    raltura = 0
    resp = input('Continuar digitando pessoas[S/N]?: ')
