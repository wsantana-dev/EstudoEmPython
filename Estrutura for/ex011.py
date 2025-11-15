#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa mostre:
#media de idade
#qual o nome do homem mais velho
#quantas mulheres tem menos de 20 anos
from datetime import date
atual = date.today().year
maior = 0
menor = 0
quantidade = 0
maior_nome = ''
totalidade = 0
media = 0
for i in range(1, 5):
    print('-' * 5, '{} PESSOA'.format(i), '-' * 5)
    nome = str(input('Nome: '))
    nascimento = int(input('Ano de Nascimento: '))
    sexo = str(input('Sexo [M/F] : ')).upper()
    print('\n')
    idade = atual - nascimento
    totalidade += idade
    media = totalidade / 4
    print('a media de idade é {}'.format(media))
    if sexo == 'M' and i == 1:
        maior = idade
        menor = idade
    else:
        if sexo == 'M' and idade > maior:
            maior = idade
            maior_nome = nome
        if sexo == 'M' and idade < menor:
                menor = idade


    if sexo == 'F' and i == 1:
        maior = idade
        menor = idade
    if sexo == 'F' and idade < 20:
        quantidade += 1
        
    
print('O homem mais velho se chama "{}"\n E ele tem {} anos de idade'.format(maior_nome, maior))
print('-=' * 50)
print('a quantidade de mulheres menores que 20 anos são {} mulheres.'.format(quantidade))


        

