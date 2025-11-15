#desenvolva um programa que leia o primerio termo e a raão de uma PA, no final, mostre os 10 primeiros termos dessa progressão

primeiro = int(input("primeiro termo: "))
razao = int(input("razão: "))
decimo = primeiro + (10 - 1) * razao

for x in range(primeiro, decimo + razao, razao):
    print(x, end=" -> ")
print("acabou")