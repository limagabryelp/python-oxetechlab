# Projeto 030
# Jogo "Adivinhe o Número"
# Tem que ser possível que: O jogador tentará adivinhar o número escolhido pelo programa, e o programa fornecerá dicas se o palpite do jogador estiver muito alto ou muito baixo.

print(f'Vamos lá! Antes de iniciarmos nosso jogo, você terá que escolher o intervalo. Preparado?\n')
a = int(input('Insira o menor número do intervalo do jogo: '))
b = int(input('Insira o maior número do intervalo do jogo: '))

import random

numero_aleatorio = random.randint(a, b)
#print(numero_aleatorio)
x = 1 - numero_aleatorio
cont = 0

print(f'O intervalo escolhido foi de {a} a {b}. Preparado?\n')

while x != numero_aleatorio:
    x = int(input('Digite um número: '))
    cont = cont + 1
    if x > numero_aleatorio:
        print('O número é maior que escolhido pelo programa.\n')
    else:
        print('O número é menor que escolhido pelo programa.\n')
   
print(f'\nVocê precisou de {cont} tentativas para acertar o número correto que era o {numero_aleatorio}!')