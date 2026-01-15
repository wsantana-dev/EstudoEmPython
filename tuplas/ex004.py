#desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. no final mostre:
#A) quantas vezes apareceu o numero 9 
#B) em que posição foi digitado o primeiro valor 3
#C) quais foram os numeros pares

while True:
    n0 = 0
    n1 = int(input('Digite um numero:'))
    n2 = int(input('Digite um numero:'))
    n3 = int(input('Digite um numero:'))
    n4 = int(input('Digite um numero:'))
    break


tupla = (n0, n1, n2, n3, n4)
    
if 9 in tupla:
    print(f'o 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O 3 foi digitado na posição {tupla.index(3)}')

for i in tupla:
    if i % 2 == 0:
        print(f'os numeros pares são {i}')


