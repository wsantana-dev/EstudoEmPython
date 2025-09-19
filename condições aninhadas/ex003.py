#escreva um programa que leia um número inteiro qualquer e peça
#para o usuário escolher qual a base de conversão
#binário, octal ou hexadecimal

num = int(input('digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('sua opção: '))
if opcao == 1:
     print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opcão invalida. Tente novamente.')