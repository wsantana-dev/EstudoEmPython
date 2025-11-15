#faça um programa que leia um numero inteiro e diga se ele é ou não um número primo
tot = 0
num = int(input("digite um numero: "))
for c in range(1, num + 1):
    if num % c == 0:
        print('\33[33m', end=" ")
        tot += 1
    else:
        print('\033[31m', end=" ")
    print(c, end=" ")
print('\n\033[m0 numero {} foi divisivel {} vezes'.format(num, tot))

