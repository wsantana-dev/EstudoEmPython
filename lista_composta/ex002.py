#crie um programa onde o usuario possa digitar sete valores numericos e cadastre-os em uma lista unica que mantenha separados os valores pares e impares. no final, mostre os valores pares e impares em ordem crescente
lista = []
prov = []

for i in range(1, 8):
    prov.append(int(input(f'Digite o {i}º valor: ')))
    lista.append(prov[:])
    prov.clear()

print(f'Os valores pares digitados foram: ', end='[')
primeiro = True # cria a variavel para controlar a hora de sair e entrar
for n in lista:
    valor = n[0]
    if valor % 2 == 0:
       if not primeiro: # se não for (True) (faça)
           print(', ', end='') #na primeira é true então não passa aqui
       print(valor, end='')
       primeiro = False #depois aqui muda e começa a liberar la encima
print(']')

print(f'Os valores impares digitados foram: ', end='[')
segundo = True
for n in lista:
    impar = n[0]
    if impar % 2 == 1:
        if not segundo:
            print(', ', end='')
        print(impar, end="")
        segundo = False
print(']')