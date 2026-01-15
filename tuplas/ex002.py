#crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol. na ordem de colocação. depois mostre:
#A) apenas os 5 primeiro colocados 
#B) os ultimos 4 colocados da tabela
#C)uma lista com os times em ordem alfabetica
#D)em que posição na tabela esta o time chapecoense

time = ('Flamengo', 'Palmeiras', 'São Paulo', 'Corinthians', 'Santos', 'Grêmio', 'Internacional', 'Atlético-MG', 'Cruzeiro', 'Botafogo', 'Fluminense', 'Vasco', 'Bahia', 'Fortaleza', 'Ceará', 'Athletico-PR', 'Red Bull Bragantino', 'Goiás', 'Cuiabá', 'América-MG', 'Chapecoense'
)

pos = time.index('Chapecoense')

print('-='*40)
print('Lista de times do Brasileirão: ', time)
print('-='*40)

print('-='*40)
print('Os cinco Primeiros são: ', time[0:6])
print('-='*40)

print('-='*40)
print('Os quatro ultimos são: ', time[-4:])
print('-='*40)

print('-='*40)
print('Os times em ordem alfabetica: ', sorted(time))
print('-='*40)

if 'Chapecoense' in time:
    print('o Chapecoense esta em: ', pos +1)
else:
    print('-='*40)
    print("o time não esta no quadro de times", pos +1)
    print('-='*40)

