# Projeto 04
# Calculadora Simples
# Tem que ser possível que: O usuário possa receber o resultado das 4 operações básicas (soma, subtração, divisão e multiplicação).

a = float(input('Insira o primeiro número: '))
print('\n1. Adição (+)\n2.Subtração (-)\n3.Divisão (/)\n4.Multiplicação (*)\n')
resposta = int(input('Digite o número da operação desejada: '))
b = float(input('\nInsira o segundo número: '))

if resposta == 1:
    soma = a + b
    print(f'\nA soma de {a} e {b} é {soma}.')
elif resposta == 2:
    subtracao = a - b
    print(f'\nA subtração de {a} e {b} é {subtracao}.')
elif resposta == 3:
    divisao = a/b
    print(f'\nA divisão de {a} por {b} é {divisao}.')
else:
    multiplicacao = a*b
    print(f'\nA multiplicação de {a} por {b} é {multiplicacao}.')