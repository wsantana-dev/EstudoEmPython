#faça um programa que leia nome e peso de cairas pessoas, guardando tudo em uma lista. no final mostre:
#a)quantas pessoas foram cadastradas
#b)uma listagem com as pessoas mais pesedas
#c) uma listagem com as mais leves.

lista = []
dado = []
mai = men = 0


while True:
    dado.append(str(input('Digite seu nome: ')))
    dado.append(float(input('Digite seu peso: ')))

    if len(lista) == 0: #se numero de indice da lista for o primeiro loop que é 0
        mai = men = dado[1] #(faça) com que o maior e o menor receba o encargo de dado[1] que é a parte da lista de peso
    else:
        if dado[1] > mai: #se o dado[1] for maior que o maior atual
            mai = dado[1] #maior recebe esse dado[1] que é maior
        if dado[1] < men: #mesma coisa porem se for menor
            men = dado[1]

    lista.append(dado[:])
    dado.clear()
    pgt = str(input('Quer Continuar? S/N ')).upper()
    if pgt in 'Nn': # Se a pergunta acima for não o laço infinito para
        break
print('-='* 30)
print(f'Foram cadastradas {len(lista)} pessoas.') #vai mostrar a contagem total da lista que é omesmo de contador
print(f'o maior peso foi {mai}Kg. peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}] ', end='')
print() #para dar um espaço
print(f'o menor peso foi {men}Kg. peso de ', end='') # esse junta com o for debaixo
for p in lista: #para cada indice=p na lista [[1], [2], [3]]
    if p[1] == men: #se encontrar o indice p[1] que é o peso que seja igual o menor
        print(f'[{p[0]}]', end='') #desse indice encontrado me traga o p[0] que é o nome






    

