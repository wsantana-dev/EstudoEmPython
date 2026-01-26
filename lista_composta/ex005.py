#faça um programa que ajude um jogador da mega sena a criar palpites. o programa vai perguntar quantos jogos serao gerados e vai sortear 6 numeros entre um e 60 para cada jogo, cadastrando tudo em uma lista composta
from random import randint
lista = []
remediadora = []
print('-'* 60)
print('JOGO DA MEGA SENA'.center(60))
print('-'* 60)
sortear = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-='* 5, f'SORTEANDO {sortear} JOGOS', '-='* 5)
contador = 0

while contador < sortear:
    for i in range(1, 7):
        remediadora.append(randint(1, 60))
    lista.append(remediadora[:])
    remediadora.clear()
    contador += 1
    
con = 1
for c in lista:
    print(f'jogo {con}: ', c)
    con += 1





