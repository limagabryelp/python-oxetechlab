# Execício de Fixação
# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:
# a) Quantos números foram digitados.
# b) A lista de valores, ordenados de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

n = int(input('Digite a quantidade de números: '))
lista = []

for i in range(n):
    lista.append(float(input('Insira um número:')))


for i in range(n):
    if (lista[i] == 5):
        print(f'O valor 5 está na posição {i}.')

lista.sort(reverse=True)
print(f'A ordem decrescente é {lista}.')