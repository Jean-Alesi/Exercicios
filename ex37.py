# Escreva um progama que leia um número inteiro qualquer
# para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
escolha = int(input('Escolha uma opção de 1 a 3: '))
binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, binario[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, octal[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hexadecimal[2:]))
else:
    print('Opção invalida.')