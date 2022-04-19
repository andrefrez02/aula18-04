segundos = int(input('Entrada:\nDigite a quantidade de segundos: '))

horas = segundos // 3600
minutos = segundos % 3600 // 60
segundos = segundos % 60

print(f'\nSaída\n{horas} horas(s), {minutos} minuto(s) e {segundos} segundo(s).')