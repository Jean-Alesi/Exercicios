# A confederação Nacional de Natação precisa
# de um programa que leia o ano de nascimento
# de um atleta e mostr sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
ano_nascimento = int(input('Qual o ano de nascimento: '))
ano_atual = int(date.today().year)
idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Você tem {} anos de idade e se enquadra na categoria de nadador {}MIRIM{}'.format(idade, '\033[1;34m', '\033[m'))
elif idade > 9 and idade <= 14:
    print('Você tem {} anos de idade e se enquadra na categoria de nadador {}INFANTIL{}'.format(idade, '\033[1;34m', '\033[m'))
elif idade > 14 and idade <= 19:
    print('Você tem {} anos de idade e se enquadra na categoria de nadador {}JUNIOR{}.'.format(idade, '\033[1;34m', '\033[m'))
elif idade > 19 and idade <= 20:
    print('Você tem {} anos de idade e se enquadra na categoria de nadador {}SÊNIOR{}.'.format(idade, '\033[1;34m', '\033[m'))
elif idade > 20:
    print('Você tem {} anos de idade e se enquadra na categoria de nadador {}MASTER{}.'.format(idade, '\033[1;34m', '\033[m'))