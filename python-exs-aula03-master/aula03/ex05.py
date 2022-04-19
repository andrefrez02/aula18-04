import math
graus = float(input('Entrada\nDigite o ângulo em graus: '))
rad = math.radians(graus)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print(f'\nSaída\n{graus}° - Radiano: {rad:.3f} - Seno: {sen:.3f} - Cosseno: {cos:.3f} - Tangente: {tan:.3f}')