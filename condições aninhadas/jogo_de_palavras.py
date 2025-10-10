
import os

palava_secreta = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1: # se for mais de uma letra é true ai entra dentro da condição if
        print('digite apenas uma letra') #se for mais de uma letra vai entrar aqui
        continue #se for false, se a letra não for maior que um continue

    if letra_digitada in palava_secreta: #se a letra_digitada estiver na palavra_secreta então:
        letras_acertadas += letra_digitada # letra_acertada '', sera atribuido + uma letra = da letra_digitada 

    palavra_formada = ''
    for letras_secretas in palava_secreta:
        if letras_secretas in letras_acertadas:
            palavra_formada += letras_secretas
        else:
           palavra_formada += '*'

    print('palavra formada:', palavra_formada)

    if palavra_formada == palava_secreta:
        os.system('cls')

        print ('VOCÊ GANHOU PARABÉNS!!')
        print('a palavra era', palava_secreta)
        print('tentativas: ', numero_tentativas)
        


