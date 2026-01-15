#crie um programa que tenha uma tupla totalmente preencida com uma contagem por extenso. de zero ate vinte
#seu programa devera ler o numero pelo teclado(entre 0 e 20) e mosrta-lo por extenso

number = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

ler = int(input('Digite um numero de 0 a 20: '))

for i in range(0, len(number)):
    if ler == i:
        print(f'Você Digitou o numero: ', number[i])
    if ler > 20:
        print('valor invalido')
        break
        