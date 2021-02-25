salario = float(input('Informe o salário do funcionário: '))

if (salario > 1250):
    novoSal = salario + salario * 0.1
    print(f'O salário teve um aumento de 10%: R${novoSal}')
else:
    novoSal = salario + salario * 0.15
    print(f'O salário teve um aumento de 15%: R${novoSal}')