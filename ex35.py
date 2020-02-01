# Escreva um programa que leia 3 retas
# e informe se é possível formar um triângulo ou não.

r1 = int(input('Digite o valor do primeira reta: '))
r2 = int(input('Digite o valor do segunda reta: '))
r3 = int(input('Digite o valor do terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os valores informados é possível formar um triângulo')
else:
    print('Com os valores informados não é possível formar um triângulo')