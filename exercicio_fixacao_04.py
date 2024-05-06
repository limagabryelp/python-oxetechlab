# Execício de Fixação
# Faça um programa que leia 5 números e informe a soma e a média dos números.

a = float(input('Insira o número: '))
soma = 0

for i in range(1,5):
    a = float(input('Insira o número: '))
    soma = soma + a

media = soma/i
print(f'A soma dos valores é {soma} e a média é {media}!')