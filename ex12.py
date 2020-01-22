prodruto = float(input('digite o valor do produto:'))
desconto = (prodruto * 5) / 100
valor = prodruto - desconto

print('Valor a pagar com o desconto aplicado é {:.2f}'.format(valor))