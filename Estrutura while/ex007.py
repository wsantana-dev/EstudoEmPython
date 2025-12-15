#escreva um programa que leia um numero n inteiro  qualquer e mostre na tela os n primeiros elementos de uma sequencia de fibonacci.

n = int(input("Digite um numero: "))
c = 0
s = 1
contador = 0
while contador < n:
    print(c, end=' ')
    soma = c + s
    c = s
    s = soma
    contador += 1
   