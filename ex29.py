#Cálculo de multa

velocidade = float(input('Digite o velocidade que passou no radar: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Você ultrapassou a velocidade permitida e foi multado em R${:.2f}'.format(multa))
else:
    print('Está dentro do limite permitido')