#aprimore o desafio anterior, mostrando no final>

#a soma todos os valores digitados 

#b a soma dos valores da terceira coluna

#c o maior valor da segunda linha 

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

soma_total = soma_coluna3 = maior_linha2 = 0

# Preenchendo a matriz
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        # a) soma de todos os valores
        soma_total += matriz[linha][coluna]

        # b) soma da terceira coluna (índice 2)
        if coluna == 2:
            soma_coluna3 += matriz[linha][coluna]

        # c) maior valor da segunda linha (índice 1)
        if linha == 1:
            if coluna == 0 or matriz[linha][coluna] > maior_linha2:
                maior_linha2 = matriz[linha][coluna]

print('-=' * 25)

# Mostrando a matriz formatada
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-=' * 25)
print(f'A soma de todos os valores é: {soma_total}')
print(f'A soma dos valores da terceira coluna é: {soma_coluna3}')
print(f'O maior valor da segunda linha é: {maior_linha2}')
