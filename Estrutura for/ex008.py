#crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.

frase = str(input("digite uma frase: ")).strip().upper() #tirou o espaço do começo e do fim usando strip e o upper deixou tudo maiusculo

palavra = frase.split() #separou palavra por palavra de uma frase
junto = ''.join(palavra) # juntou com '' espaços juntos podia ser '*' ia se conectar com*as*estrelas*no*meio 
inverso = ''
for letra in range(len(junto) - 1, -1, -1): #para pegar letra por letra da variavel junto 
    inverso += junto[letra]
if inverso == junto:
    print(f'a frase {junto} e {inverso} são iguais \n então temos um palindromo')
else:
    print(f"a frase {junto} e {inverso} NÃO são iguais \n então logo Não temos um palindromo")



