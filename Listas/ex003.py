#crie um programa aonde o usuario pode digitar 5 valores numericos e cadastre-os em uma lista. ja na posição correta de inserção(sem uso de sort()) no final mostre a lista ordenada na tela
lista = []

n1 = int(input('Digite um valor: '))
print('adicionado ao final da lista...')
lista.append(n1)

for i in range(1, 5):
    num = int(input('Digite outro valor: '))

    if num > lista[-1]:
        print('adicionando no final')
        lista.append(num)

    elif num < lista[0]:
        print('adicionando no inicio')
        lista.insert(0, num)

    else:
        pos = 0
        while pos < len(lista): #enquato o contator for menor que o tamanho da lista
            if num <= lista[pos]: # se o numero for menor ou igual ao local por onde estamos andando na lista
                print('adicionando no meio...') #adicionamos esse numero no meio
                lista.insert(pos, num) #na posição atual inserimos o numero
                break
            pos += 1

print(lista)

    