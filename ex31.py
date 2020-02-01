print('-=-'*10)
print('Sistema para Cálculo de viagem')
print('-=-'*10)
passagem = float(input('Digite a distância em km para cálculo da passagem: '))
km1 = 0.50 * passagem
km2 = 0.45 * passagem

if passagem > 200:
    print('Para essa viagem, o valor a ser cobrado será de R${}{}{}'.format('\033[1;32m', km2, '\033[m'))
else:
    print('Para essa viagem, o valor a ser cobrado será de R${}{}{}'.format('\033[1;32m', km1, '\033[m'))