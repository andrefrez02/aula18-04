valor = float(input('Entrada:\nDigite o valor da hora aula: R$'))
carga = int(input('Digite a carga horária semanal: '))

salario_base = valor * carga * 4.5
adicional = salario_base * 1/6
salario = salario_base + adicional

print(f'\nSaída:\nSalário final: R${salario:.2f}')