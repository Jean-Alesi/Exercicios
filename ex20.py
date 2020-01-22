import random

n1 = input('Primeiro trabalho: ')
n2 = input('Segundo trabalho: ')
n3 = input('Terceiro trabalho: ')
n4 = input('Quarto trabalho: ')

lista = [n1, n2, n3, n4]
random.shuffle(lista)

print('A ordem de apresentação será\n {}'.format(lista))