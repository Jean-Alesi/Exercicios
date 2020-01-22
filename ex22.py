nome = input('Digite seu nome:').strip()
#tam = len(nome.strip())
div = nome.split()
#nomes = nome.strip()

#print(nomes.upper())
#print(nome.lower())
#print(tam)
#print(len(div[0]))

print('Seu nome em maiúsculo: {}'.format(nome.upper()))
print('Seu nome em minúsculo: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome.strip())))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro nome tem {} caracteres'.format(len(div[0])))


