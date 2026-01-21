num = [2, 5, 9, 1]
num[2] = 3      #no indice 2 troque o valor por 3
num.append(7)   #adicione esse numero ao final da lista 
num.sort(reverse=True)  #coloque em ordem do maior para o menor
num.insert(2, 0)  #adicione no indice 2 o numero zero, o valor que estava no indice dois vai para frente
num.pop()  #remova o ultimo valor
num.remove(2) #ele remove o numero 2, esse não vai por indice
print(num)
print(f'essa lista tem {len(num)} elementos')  #len conta a quantidade de indices desde 0
if 10 in num:
    num.remove(10)
else:
    print("não achei o numero 10 ")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for p, v in enumerate(valores):
    print(f'na posição {p} encontrei o valor {v}!')  # o p ele acha a posiçao e o v ele acha o valor
print('cheguei ao final da lista')