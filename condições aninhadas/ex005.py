#faça um programa que leia o ano de nascimento de um jovem e informa, de acordo com sua idade:
#se ele ainda vai se alistar ao serviço militar
#se é a hora de se alistar
#se já passou do tempo de alistamento
#seu programa também devera mostrar o tempo que falta ou que passou do prazo

age = int(input('qual sua idade? '))

if age < 18:
    print('você pode se alistar somente aos 18 anos')
    print('ainda te falta {} anos'.format((18 - age)))
elif age == 18:
    print('você ja pode se alistar')
else:
    print('voce ja passou do prazo de alistamento')
    print('voce ja passou {} anos'.format((age - 18)))


