# Elabore um programa que calcule o valor a ser
# pago por um produto, considerando o seu preço
# normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros.
from time import sleep
print('-=-'*20)
print('\033[1;31m', 'Cálculo de valor do produto de acordo com o pagamento', '\033[m')
print('-=-'*20)

valor_original = float(input('Informe o valor do produto: '))
sleep(2)
print('Qual é a forma de pagamento que deseja?')
sleep(1)
print('Digite 1 para pagamento {}À VISTA NO DINHEIRO{} com 10% de desconto.'.format('\033[1;33m', '\033[m'))
sleep(1)
print('Digite 2 para pagamento {}À VISTA NO CARTÃO{} com 5% de desconto.'.format('\033[1;33m', '\033[m'))
sleep(1)
print('Digite 3 para pagamento {}ATÉ 2X NO CARTÃO{}. Valor normal sem desconto e sem juros'.format('\033[1;33m', '\033[m'))
sleep(1)
print('Digite 4 para pagamento em {}3x OU MAIS NO CARTÃO{} com acréscimo de 20% de juros.'.format('\033[1;33m', '\033[m'))
sleep(1)

forma_pagamento = int(input('Escolha de 1 a 4 a forma de pagamento: '))
pg1 = valor_original - ((valor_original * 10) / 100)
pg2 = valor_original - ((valor_original * 5) / 100)
pg3 = valor_original
pg4 = valor_original + ((valor_original * 20) / 100)

if forma_pagamento == 1:
    print('{}Valor final do produto com desconto de 10% aplicado é R${:.2f}{}'.format('\033[1;31m', pg1, '\033[m'))
elif forma_pagamento == 2:
    print('{}O valor final do produto com o desconto de 5% aplicado é R${:.2f}{}'.format('\033[1;31m', pg2, '\033[m'))
elif forma_pagamento == 3:
    print('{}O valor a ser pago é R${:.2f}{}'.format('\033[1;31m', pg3, '\033[m'))
elif forma_pagamento == 4:
    print('{}O valor final do produto com juros de 20% aplicado é R${:.2f}{}'.format('\033[1;31m', pg4, '\033[m'))
