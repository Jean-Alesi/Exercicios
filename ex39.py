# O programa irá ler um ano de nascimento de um jovem e informar,
# de acordo com a sua idade:
# se ele ainda vai se alistar;
# se é a hora de se alistar;
# se já passou do tempo do alistamento.
# o programa também deverá mostrar o tempo que falta ou que passou do prazo.


from _datetime import date
ano_nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
alistamento = int(ano_nascimento + 18)

if idade == 18:
    print('Quem nasceu {} tem {} anos e já está no ano de alismento.'.format(ano_nascimento, idade))
elif idade < 18:
    print('Quem nasceu {} tem {} anos e ainda faltam {} anos para o seu alistamento'.format(ano_nascimento, idade, 18 - idade))
elif idade > 18:
    print('Quem nasceu {}, tem {} anos e o ano de alistamento foi em {}.'.format(ano_nascimento, idade, alistamento))


