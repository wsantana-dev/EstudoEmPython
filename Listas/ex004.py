#crie um programa que vai ler varios numeros e colocar em uma lista depois disso mostre:
#a) quantos numeros foram digitados
#b) a lista de valores, ordenada de forma decrescente
#c)se o valor 5 foi digitado e esta ou não na lista

pos = 0
lista = []
pgt = 'S'
while pgt == 'S':
    num = int(input('digite um valor: '))
    pgt = str(input('deseja continuar? S/N ')).upper()
    lista.append(num)
    lista.sort(reverse=True)
    pos += 1
    print(f'foram digitados {pos} numeros\n {lista}')
    
if 5 in lista:
        posicao = lista.index(5)
        print(f'existe o 5 na lista ele esta na posição {posicao +1}')
else:
        print('o numero 5 não esta na lista')
    
    