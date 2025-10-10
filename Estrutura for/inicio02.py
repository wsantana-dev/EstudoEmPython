n = int(input('digite um numero: '))

for c in range(0, n):
    print(c)
print('fim')

for c in range(0, 3):
    n = int(input('digite um numero:'))
print('fim')



s = 0   #criou a variavel com o valor de zero

for c in range(0, 4): # para controlador in range(0,4): -- laço controlador c no intervalo de (0, 4): faça
    n = int(input('digite um numero')) # 4X repetir isso
    s += n # s = s + n --- o valor de s vai ser atribuido toda vez que chegar nele, e logo depois na proxima repetiçao vai somar com o prox n
print('a somatoria dos numeros é {}'.format(s))