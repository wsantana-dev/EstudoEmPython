#crie um programa que leia varios numeros inteiros pelo teclado. o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada. no final moste, quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)

conta = 0
soma = 0 
n = 0

while n != 999:
    n = int(input('Digite o numero: '))
    if n != 999:
        conta += 1
        soma += n

if n == 999:
    print(f'A quantidade de numeros digitados foram {conta} e a soma entre eles são {soma}')
