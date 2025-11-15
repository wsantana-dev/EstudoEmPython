#desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor digitado for impar, desconsidere-o

i = 0

for c in range(1, 7):
    num = int(input('digite um valor: '))
    if num % 2 == 0:
        i += num
        
print(i)