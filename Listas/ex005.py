#crie um programa que vai ler varios numeros e colocar em uma lista. depois disso , crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente
#ao fonal mostre o conteudo das tres listas geradas

lista = []
lista_par = []
lista_impar = []

pgt = 'S'
while pgt == 'S':
    num = int(input('Digite um numero: '))
    pgt = str(input('Gostaria de Continuar? S/N ')).upper()
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f'essa é a lista {lista}\nessa é a lista par {lista_par}\nessa é a lista impar {lista_impar}')

