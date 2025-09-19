#faça um programa que veja cada tamanho de uma linha e veja se forma um triângulo
#e se é Equilátero: todos lados iguais
#se é Isósceles: dois lados igual
#Escaleno: todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar um triangulo', end='')
    if r1 == r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')

else:
    print('os segmentos acima NÃO podem formar um triangulo')

