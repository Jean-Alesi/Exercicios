#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quandaditade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar sabendo que a diaria é R$60 e o preço por km rodado é R$0,15

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km você rodou com o carro? '))
vd = 60 * dias
vkm = 0.15 * km

print('Valor das diárias: R${:.2f}'.format(vd))
print('Valor por km rodado: {}'.format(vkm))
print('Valor total da locação: R${:.2f}'.format(vd + vkm))
