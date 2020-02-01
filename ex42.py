# Refaça o desafio 35 dos triângulos, acrescentando o recurso de
# mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento: '))
r3 = float(input('Digite o terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O seguimentos informados podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os seguimentos informados não podem formar um triângulo.')