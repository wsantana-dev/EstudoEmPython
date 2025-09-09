#crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
#com a média atingida
#média abaixo de 5.0: reprovado
#média entre 5.0 e 6.9: recuperação
#média 7.0 ou superior: aprovado

noteOne = float(input('digite qual foi sua primeira nota: '))
noteTwo = float(input('digite qual foi sua segunda nota: '))
average = (noteOne + noteTwo) / 2

if average < 5:
    print('REPROVADO')
elif average < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')