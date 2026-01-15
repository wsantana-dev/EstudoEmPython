#crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.
#depois disso mostre a listagem de numeros gerados e tambem indique o menor e o maior valor que estão na tupla
from random import randint

n1 = randint(1, 5)
n2 = randint(1, 5)
n3 = randint(1, 5)
n4 = randint(1, 5)
n5 = randint(1, 5)

num = (n1, n2, n3, n4, n5)
print('A listagem de numeros é: ', num, end="")

maior = max(num)
menor = min(num)

print(f'\no maior numero é {maior} e o menor é {menor}')