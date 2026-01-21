#faça um programa que leia 5 valores numericos e guarde os em uma lista no final mostra qual é o maior e o menor valor digitado e as suas respectivas posiçoes na lista
lista = []

for i in range(0, 5):
    valor = int(input('digite um numero: '))
    lista.append(valor)
print('-=' *30)
print(f'Os valores Digitado na lista são: {lista} ')

maior = max(lista)
menor = min(lista)

localiza_maior = lista.index(maior)
localiza_menor = lista.index(menor)

print(f'O maior valor é {maior} encontrado na posição {localiza_maior}\ne o menor valor é o {menor} localizado na posição {localiza_menor} da lista')
