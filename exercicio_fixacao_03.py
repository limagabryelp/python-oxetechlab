# Execício de Fixação
# Escreva um programa em Python que solicite ao usuário um número inteiro. Em seguida, verifique se o número é par ou ímpar e exiba uma mensagem adequada.

numero = int(input('Insira um número inteiro: '))

if (numero%2 == 0):
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))