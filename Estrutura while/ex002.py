#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um numero de 0 e 10. só que agora o jogador vai tentar adivinhar qté acerta, mostrando no final quantos palpites foram necessarios para vencer

from random import randint

num = randint(0, 10)


tentativa = int(input('digite um numero de 0 a 10: '))


if tentativa == num:
    print(f'PARABÉNS VOCÊ ACERTOU o numero é o {num}')


while tentativa != num:
    print('Errou o numero do computador'.format(num))
    tentativa = int(input('TENTE NOVAMENTE: '))
    if tentativa == num:
        print('Parabéns, ACERTOU!!')
    
