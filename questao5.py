num1 = float(input('Informe o 1° número: '))
num2 = float(input('Informe o 2° número: '))
operacao = input('Informe a operação a ser feita: ')

if operacao == '+':
    print(f'{num1} {operacao} {num2} = {num1 + num2}')
elif operacao == '-':
    print(f'{num1} {operacao} {num2} = {num1 - num2}')
elif operacao == '*':
    print(f'{num1} {operacao} {num2} = {num1 * num2}')
elif operacao == '/':
    print(f'{num1} {operacao} {num2} = {num1 / num2}')
else:
    print('Operação inválida!')