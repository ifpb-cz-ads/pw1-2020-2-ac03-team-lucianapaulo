#6) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa.
#O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
#O valor da prestação mensal não pode ser superior a 30% do salário.
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input('Qual o valor da casa que deseja comprar?'))
valor_anos = float(input('Em quantos anos deseja comprar essa casa?'))
valor_salario = float(input('Qual o seu salário?'))

valor_prestacao_mensal = valor_casa / (valor_anos * 12)
if valor_prestacao_mensal > (valor_salario * 0.3):
  print('Infelimente seu salário é muito baixo para pagar as prestações, aumente seu salario, o número de anos ou procure uma casa mais barata')
else:
  print('Emprestimo aprovado com sucesso!')