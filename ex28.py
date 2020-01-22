import random
num = [0, 1, 2, 3, 4, 5]
computador = random.choice(num)

jogo = input('Tente adivinhar o número de 0 a 5 que o computador escolheu: ')
if jogo == computador:
    print('Você acertou, PARABÉNS!')
else:
    print('Você ERROU!')