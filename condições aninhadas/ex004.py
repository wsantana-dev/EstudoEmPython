#escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#o primeiro valor é maior
#o segundo valor é maior
#não existe valor maior, os dois são iguais

print('-=' * 20)
print('VAMOS VER QUAL VALOR É MENOR OU MAIOR')
print('-=' * 20)

firstNumber = int(input('digite o primeiro valor: '))
secondNumber = int(input('digite o segundo valor: '))

firstmax = max(firstNumber, secondNumber)



if firstNumber > secondNumber or firstNumber < secondNumber:
    print(f'O numero maior entre os dois é {firstmax}')
elif firstNumber == secondNumber:
    print('os dois são igual')


