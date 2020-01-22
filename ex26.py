frase = input('Digite uma frase:').strip()

print('A sua frase possui {} letas "a"'.format(frase.upper().count('A')))
print('Em que posição a primeira letra "a" se encontra? {}'.format(frase.upper().find('A')+1))
print('Em que posição a última letra "a" aparece? {}'.format(frase.upper().rfind('A')+1))