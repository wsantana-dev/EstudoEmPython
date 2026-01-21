#crie um programa onde o usuario digite uma expressão qualquer que use parenteses. seu aplicativo devera analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta.

exp = str(input('Digite sua expressão: '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('esta valido')
else:
    print('esta invalido') 

