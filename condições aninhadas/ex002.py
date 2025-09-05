#escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#o programa vai perguntar o valor da cada, o salário do comprador
#e em quantos anos ele vai pagar
#calcule o valor da prestação mensal =, sabendo que ela não pode exceder 30% do salario ou então
#o empréstimo sera negado

valor = float(input('qual o valor da casa? '))
salario = float(input('qual seu salario? '))
anos = float(input('quantos anos vai pagar? '))
meses = anos * 12
parcela = valor / meses
porcentagem = salario * (30 / 100)

print('-=' * 25)
print(f'o valor da sua parcela vai ficar em R${parcela:.2f}')
print('-=' * 25)

if parcela > porcentagem:
    print(f'O valor total da sua parcela ultrapassa os 30% pedido que seria R${porcentagem} ')
elif parcela < porcentagem:
    print('o valor da sua parcela esta menor que os 30% do seu salario')
else:
    print('algo foi digitado errado')