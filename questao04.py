#4) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.

distancia = float(input('Qual a distância em km que deseja percorrer?'))

if distancia > 200:
  valor_passagem = distancia * 0.45
else:
  valor_passagem = distancia * 0.5
print(f'Você deverá pagar R${valor_passagem}')