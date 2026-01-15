#crie um programa que tenha umatupla unica com nome de produtos e seus respectivos preços na sequencia. 
#no final mostre uma listagem de preços organizando od dados em forma tabular

produto = ("Lápis", 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Tranferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Caneta', 22.30, 'Livro', 34,90)

print("-"*50)
print('LISTAGEM DE PREÇO'.center(50))
print("-"*50)

for i in produto[1::2]:
    indice = produto.index(i) - 1
    print(produto[indice], f'.' *30, 'R$', i)
    