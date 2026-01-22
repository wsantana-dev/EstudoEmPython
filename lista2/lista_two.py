#objetivo dessaaula é aprender listas dentro de listas 
#ponto importante [:] isso copia uma lista se não colocar isso vai fazer uma conexão entre listas

galera = [['João', 19], ['Lucas', 19], ['Mike', 20], ['will', 15]]
print(galera[0]) #vai mostrar joao 19
print(galera[0][1])#vai mostrar 19
print(galera[3][0]) #vai mostrar will
print(galera[0:2]) #as duas primeiras

#for p in galera:
#    print(p)    # vai retornar a lista completa 

for p in galera:
    print(p[0]) #vai retornar somente os itens 0 da lista toda

for p in galera:
    print(f'{p[0]} tem {p[1]} de idade.') #vai retornar os itens tratados 

pessoal = []
dado = [] #lista secundaria para ser passada para dentro de pessoal.

for c in range(0, 3): 
    dado.append(str(input('Nome: '))) #dado armazena na lista o nome
    dado.append(int(input('Idade: '))) #dado armazena na lista a idade
    pessoal.append(dado[:]) #cria uma copia e repete conforme o indice la no for
    dado.clear() #limpa os dados da lista dado no final
print(pessoal)

totalmaior = totalmenor = 0 # (variavel para contar) ao inves de fazer duas separas ja juntou elas

for p in pessoal:
    if p[1] > 21:
        print(f'{p[0]} é maior de idade.')
        totalmaior += 1                   #contador somando
    else:
        print(f'{p[0]} é menor de idade')
        totalmenor += 1

print(f'a quantidade de pessoas maiores são de: {totalmaior}\n'
        f'e a de menor é {totalmenor}'
        )


