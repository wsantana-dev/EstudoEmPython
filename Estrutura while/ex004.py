#faça um programa que leia um numero qualque e mostre seu fatorial
# 5! = 5x4x3x2x1

valor = int(input('Digite um valor: '))
contado = 1

while valor > 0:
    contado = contado * valor
    print(valor, end='')
    valor -= 1
    if valor > 1:
        print('x', end='')
    else:
        print('=', end='')
    print(contado)
    