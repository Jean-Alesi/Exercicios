        #Digite o nome de um cidade e eu te digo se ela começa com Santo

cidade = input('Digite o nome da sua cidade natal:').strip()
div = cidade.upper().split()
print('A sua cidade natal Começa com Santo? {}'.format('SANTO' in div[0]))