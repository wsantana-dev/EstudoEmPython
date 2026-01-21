#crie um programa aonde o usuario possa digitar varios valores numericos e cadastra-os numa lista. caso o numero ja exista la dentro, ele não sera adicionado. no final serão  exibido todos os valores unicos digitados em ordem crescente
lista = []
pgt = str(input('quer colcoar numero: ')).upper()
while pgt == 'S':
    num = int(input('Digite um numero: '))
    pgt = str(input('quer continuar? [S/N] ')).upper()
    if num in lista:
        print('ja tem esse numero')
    else:
        lista.append(num)  
    lista.sort() 

print(lista)
    