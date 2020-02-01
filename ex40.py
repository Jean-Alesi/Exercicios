# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO


av1 = float(input('Nota da AV1: '))
av2 = float(input('Nota da AV2: '))
media = float(av1 +av2) / 2

if media >= 5 and media < 7:
    print('Sua média final foi {:.1f}. Caro aluno, você está de RECUPERAÇÃO.'.format(media))
elif media < 5:
    print('Sua média foi {:.1f}. Caro aluno, você foi REPROVADO.'.format(media))
elif media > 7:
    print('Sua média foi {:.1f}. Caro aluno, você foi APROVADO.'.format(media))




