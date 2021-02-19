vel = float(input('Informe a velocidade do carro em km/h: '))

if vel > 80:
    multa = (vel - 80) * 5
    print(f'Você foi multado no valor de R${multa}')