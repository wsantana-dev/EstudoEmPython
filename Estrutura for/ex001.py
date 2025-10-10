#faça um programa que moste na tela uma contagem regreciva para o estouro de fogos de artificio, indo de 10 até 0, com uma pausa de um segundo

from time import sleep

for c in range(10, -1, -1):
    sleep(1)
    print(c)

print("🎆")

