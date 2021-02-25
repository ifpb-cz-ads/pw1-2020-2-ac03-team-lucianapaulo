#2) Escreva um programa que leia três números e que imprima o maior e o menor.

a = int(input('Digite um número:'))
b = int(input('Digite um número:'))
c = int(input('Digite um número:'))

menor, maior = a,a

if menor > b:
  menor = b
if menor > c:
  menor = c
if maior < b:
  maior = b
if maior < c:
  maior = c
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')