print('-=-'*20)
print('Sistema Aprovador para Financiamento de Imóvel')
print('-=-'*20)

casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o valor da sua renda atual? '))
financiamento = float(input('Em quantos anos deseja pagar? '))

parcela = int(12 * financiamento)
valor = casa / parcela
porcentagem = (valor * 100) / salario

if porcentagem > 30:
    print('Caro cliente, infelismente o seu financiamento foi','\033[1;31m','NEGADO', '\033[m', 'devido a parcela exceder 30% da sua renda.')
else:
    print('Caro cliente, o seu financiamento foi', '\033[1;32m', 'APROVADO', '\033[m')
print('O seu financiamento ficou em {}{}{}x de R${}{:.2f}{}.'.format('\033[7;30m', parcela, '\033[m', '\033[7;30m', valor, '\033[m'))


