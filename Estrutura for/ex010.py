#faça um programa que leia o peso de cinco pessoas. no final, mostre qual foi o maior e o menor peso lido
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("digite o {}ª peso: ".format(p)))
    if p == 1: #no primeiro range faça
        maior = peso #como não tem outro valor os dois vão ser o maior e o menor
        menor = peso
    else:
        if peso > maior: #se o peso for maior que o ultimo maior faça
            maior = peso #o maior recebe o novo peso maior
        if peso < menor:
            menor = peso

print('o menor peso digitado foi {}'.format(maior))
print('e o menor peso digitado foi {}'.format(menor))

