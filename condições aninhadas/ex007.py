#a confederação nacinal de natação precisa de um programa que leia o ano
#de nascimento de um atleta e mostre sua categoria de acordo com idade
#até 9 anos: mirim
#até 14 anos: infantil
#até 19 anos: junior
#até 20 anos: sênior
#acima: master

age = int(input('digite sua idade: '))

if age <= 9:
    print('Mirim')
elif age <= 14:
    print('infantil')
elif age <= 19:
    print('Junior')
elif age <= 20:
    print('Senior')
else:
    print('Master')