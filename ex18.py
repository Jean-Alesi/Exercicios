import math

ang = float(input('Informe o valor do ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang,tangente))