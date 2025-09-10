#crie um programa que faça o computador jogar jokepô com você

from random import randint

myChoice = str(input('Digite pedra, papel ou tesoura: '))

choiceComputer = randint(0, 2)

pcStone = choiceComputer == 0
pcPaper = choiceComputer == 1
pcScissors = choiceComputer == 2

if pcStone:
    print('Computador: pedra')
elif pcPaper:
    print('Computador: papel')
elif pcScissors:
    print('Computador: tesoura')
else:
    print('erro')

if myChoice == 'pedra' and pcStone:
    print('\033[1;33mEMPATE\033[m')
elif myChoice == 'papel' and pcPaper:
    print('\033[1;33mEMPATE\033[m')
elif myChoice == 'tesoura' and pcScissors:
    print('\033[1;33mEMPATE\033[m')

if myChoice == 'pedra' and pcScissors:
    print('\033[1;32mVocê Ganhou!!!\033[m')             #PEDRA VS TESOURA
elif myChoice == 'tesoura' and pcStone:
    print('\033[1;31mPC Ganhou!!!\033[m')
elif myChoice == 'papel' and pcStone:
    print('\033[1;32mVocê Ganhou!!!\033[m')             # PEDRA VS PAPEL
elif myChoice == 'pedra' and pcPaper:
    print('\033[1;31mPC Ganhou!!!\033[m')
elif myChoice == 'tesoura' and pcPaper:
    print('\033[1;32mVocê Ganhou!!!\033[m')              #TESOURA VS PAPEL
elif myChoice == 'papel' and pcScissors:
    print('\033[1;31mPC Ganhou!!!\033[m')