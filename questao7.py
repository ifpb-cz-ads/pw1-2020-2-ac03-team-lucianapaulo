kwh = float(input('Informe a quantidade de kWh consumida: '))

inst = input('Informe o tipo de instalação: ').upper()

if inst == 'R':
    faixa = 0.65 if kwh > 500 else 0.4
    
    print(f'O total a pagar é de: R${kwh * faixa}')
elif inst == 'I':
    faixa = 0.6 if kwh > 5000 else 0.55
    
    print(f'O total a pagar é de: R${kwh * faixa}')
elif inst == 'C':
    faixa = 0.6 if kwh > 1000 else 0.55
    
    print(f'O total a pagar é de: R${kwh * faixa}')
else:
    print('Tipo de instalação inválido!')