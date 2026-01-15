#crie um programa que tenha uma tupla com varias palavras(nao usar acentos).
#depois disso, voce deve mostrar, para cada palavra , quais são suas vogais

palavras = ('manga', 'banana', 'ameixa', 'abacaxi', 'pera', 'coco', 'laranja', 'morango')

for i in palavras:
    print(f'\nna palavra {i} temos as vogais', end= ' ')
    for letras in i:
        if letras in "aeiou":
            print(letras, end=" ")
    