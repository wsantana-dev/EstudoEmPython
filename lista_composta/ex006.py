#crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta. no final, mostre um boletim contendo a media de cada um e permita que  o usuario possa  mostrar as notas de cada aluno individualmente

lista = []
comp = []


contador = 0
while True:
    comp.append(str(input('Nome: ')))
    comp.append(float(input('Nota: ')))
    comp.append(float(input('Nota: ')))
    lista.append(comp[:])
    comp.clear()

    pgt = str(input('Quer Continuar? S/N '))
    contador += 1
    if pgt in 'Nn':
        break

print('-='* 20)
print(f'{"Nº":<10}{"nome":<10}{"Média":<5}')
print('-'* 40)


for pos, d in enumerate(lista):
    nota1 = d[1]
    nota2 = d[2]
    media = (nota1 + nota2) / 2
    print(f'{pos:<10} {d[0]:<10} {media:<5}')

print('-'* 40)

while True:
    num = int(input('Quer ver as notas de qual aluno? (999 interrompe) '))

    if num == 999:
        print('Encerrando...')
        break

    if 0 <= num < len(lista): # Se o número digitado for maior ou igual a 0
#e menor que o tamanho da lista”
                        #lista[o numero pelo input] [com o indice de pesso]
        print(f'Notas de {lista[num][0]}: {lista[num][1]} e {lista[num][2]}')
    else:
        print('Número de aluno inválido')







