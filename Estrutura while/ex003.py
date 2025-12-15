# Crie um programa que leia DOIS VALORES E MOSTRE um menu na tela:
# [1] SOMAR
# [2] MULTIPLICAR
# [3] MAIOR
# [4] NOVO NUMERO
# [5] SAIR DO PROGRAMA
#SEU PROGRAMA DEVERA REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO
from time import sleep
opcao = 0
n1 = int(input('DIGITE O PRIMEIRO NUMERO: '))
n2 = int(input('DIGITE O SEGUNDO NUMERO: '))
menu = ('\nMENU DE AÇÃO:\n [1] SOMAR\n [2] MULTIPLICAR\n [3] MAIOR\n [4] NOVO NUMERO\n [5] SAIR DO PROGRAMA\n')

while opcao != 5:
    print(menu)
    opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
    
    if opcao == 1:
        print(f'\nA SOMA DOS NUMEROS SÃO:\n {n1} + {n2} = {n1 + n2}')

    if opcao == 2: 
        print(f'\nA MULTIPLICAÇÃO ENTRE OS NUMEROS SÃO:\n {n1} X {n2} = {n1 * n2}')
        
    if opcao == 3:
        if n1 > n2:
            print(f'\nEntre os dois o {n1} é maior!!!')
        if n2 > n1:
            print(f'\nEntre os dois o {n2} é maior!!!')
    if opcao == 4: 
        n1 = int(input('DIGITE O PRIMEIRO NUMERO: '))
        n2 = int(input('DIGITE O SEGUNDO NUMERO: '))
print('Você saiu do programa!!')