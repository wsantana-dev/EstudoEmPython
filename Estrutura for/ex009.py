#crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são de maiores coloque que a maior idade seja 21 anos

from datetime import date #para importar o ano 
atual = date.today().year #ano atual
totmaior = 0
totmenor = 0

for pess in range(1, 8):
   nasc = int(input("qual o ano a {}ª pessoa nasceu?: ".format(pess)))
   idade = atual - nasc
   if idade >= 21:
      totmaior += 1 #vai  somando a quantidade de pessoas maiores
   else:
      totmenor += 1
print("ao todo tivemos {} pessoas maiores de idade".format(totmaior))
print("ao todo tivemos {} pessoas menores de idade".format(totmenor))