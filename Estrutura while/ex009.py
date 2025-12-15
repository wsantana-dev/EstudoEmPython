#crie um programa que leia varios numeros inteiros pelo teclado. no final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido. o programa deve perguntar ao usuario se ele quer continuar a digitar valores.
conta = 0
soma = 0
maior = 0
menor = 0
pgt = str(input('Quer digitar numeros? SIM/NAO ')).upper()
while pgt == 'SIM':
    n = int(input('Digite um numero: '))
    conta += 1
    soma += n
    if conta == 1:
        menor = n
        maior = n
    if conta != 1:
        if n > maior:
            maior = n
        if n < menor: 
            menor = n
    pgt = str(input('Quer digitar numeros? SIM/NAO ')).upper()

media = soma / conta


print(f'o menor numero lido foi: {menor}')
print(f'o maior numero lido foi: {maior}')
print(f'a média dos numeros digitados é: {media}')
    