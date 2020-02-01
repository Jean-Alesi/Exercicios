# Desenvolva uma lógica que leia o peso e altura
# de uma pessoa, calcule seu IMC e mostre seu status,
# de acordo com a tabala abaixo:
# Abaixo de 18.5: Abaixo do peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40 : Obesidade;
# Acima de 40: Obesidade móbida.

print('-=-' * 15)
print('\033[1;31m', 'Calcule seu IMC e Descubra seu status atual', '\033[m')
print('-=-' * 15)

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = float(peso / (altura * altura))

if imc <= 18.5:
    print('Seu IMC é {:.1f}. Você está abaixo do peso, considere ganhar mais alguns quilos.'.format(imc))
elif imc > 18.5 and imc <= 25:
    print('Seu IMC é {:.1f}. Você está no peso ideal, PARABÉNS!'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC é {:.1f}. Você está com sobrepeso, considere fazer um regime.'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC é {:.1f}. Você está obeso, por questão de saúde faça urgente um regime.'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.1f}. Você se encontra no quadro de obesidade móbida, e precisará de acompanhamentos médicos.'.format(imc))

