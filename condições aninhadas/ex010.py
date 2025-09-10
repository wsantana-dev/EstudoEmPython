#Elabore um programa que calcule o valor a ser pago por um produto
#considerando seu preço normal e condição de pagamento
#a vista dinheiro/cheque: 10% de desconto
#Á vista no cartão: 5% de desconto
#em até 2x no carão: preço normal
#3x ou mais: 20% de juros

from colorama import *

video_game = 1500.0

print('--=' * 25)
print('\033[1;36mESTAMOS VENDENDO UM VÍDEO GAME POR R$1500.00, TENDO INTERESSE DIGITE UMA DAS OPÇÕES A SEGUIR:\033[m')
print('--=' * 25)

print('\033[0;34m1. Dinheiro/ cheque\033[m')
print('\033[0;34m2. À vista no cartão\033[m')
print('\033[0;34m3. Parcelado em Duas Vezes\033[m')
print('\033[0;34m4. Parcelado em mais de 3X\033[m')


pagamento = str(input('\033[4;33mSELECIONE A FORMA DE PAGAMENTO: \033[m'))




if pagamento == '1':
    desconto = video_game * 10 / 100
    video_game -= desconto
    print('voce teve 10% de desconto e vai ficar R${:.2f}'.format(video_game))
elif pagamento == '2':
    desconto = video_game * 5 / 100
    video_game -= desconto
    print(f'Á vista no cartão liberamos o desconto de 5%, valor total é de R${video_game:.2f}')
elif pagamento == '3':
    print(f'parcelado em até duas vezes no cartão fica o valor normal de: R${video_game:.2f}')
else:
    juros = video_game * 20 / 100
    video_game += juros
    print(f'parcelado em mais de duas vezes fica no total de: R${video_game:.2f}')

