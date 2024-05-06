# Execício de Fixação
# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

def soma(num1, num2, num3):
    soma = num1 + num2 + num3
    return soma

a = float(input('Insira um número: '))
b = float(input('Insira um número: '))
c = float(input('Insira um número: '))

resultado_soma = soma(a, b, c)

print(f'A soma dos três argumentos é igual a {resultado_soma}!')