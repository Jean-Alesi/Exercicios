# Crie um programa que faça a máquina jogar
# jokenpo com o usuário

print('-=-'*10)
print('Vamos jogar JO KEN PO')
print('-=-'*10)

from random import choice
from time import sleep
jogo = ['Pedra', 'Papel', 'Tesoura']
maquina = choice(jogo)
usuario = str(input('Pedra, Papel ou Tesoura? ')).upper().strip()
print('\033[1;31m', 'JO', '\033[m')
sleep(1)
print('\033[1;31m', 'KEN', '\033[m')
sleep(1)
print('\033[1;31m', 'PO', '\033[m')
sleep(2)
print('\033[1;34m', usuario, '\033[m')
sleep(1)
print('\033[1;33m', maquina, '\033[m')

if maquina == 'Pedra' and usuario == 'PAPEL':
    print('PERDI, fui embrulhado!')
elif maquina == 'Pedra ' and usuario == 'TESOURA':
    print('GANHEI, Te Quebrei!')
elif maquina == 'Papel' and usuario == 'PEDRA':
    print('GANHEI, Te Embrulhei!')
elif maquina == 'Papel' and usuario == 'TESOURA':
    print('PERDI, fui cortado!')
elif maquina == 'Tesoura' and usuario == 'PEDRA':
    print('PERDI, Fui Quebrado!')
elif maquina == 'Tesoura' and usuario == 'PAPEL':
    print('GANHEI, Te Cortei!')
else:
    print('Empate, vamos de novo?')