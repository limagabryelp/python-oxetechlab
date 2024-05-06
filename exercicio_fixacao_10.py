# Execício de Fixação
# Faça um programa, que realize a soma dos elementos da tupla e mostre os elementos da tupla logo após o resultado da soma.

tupla_lista = input('Digite uma lista de números separados por uma vírgula: ').split(',')

lista_numeros = [float(num) for num in tupla_lista]

soma = sum(lista_numeros)

print(f'A soma dos números {lista_numeros} é {soma}!')