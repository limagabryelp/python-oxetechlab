# Execício de Fixação
# Escreva um programa em Python que solicite ao usuário o seu nome e a sua idade. Em seguida, exiba uma mensagem de boas-vindas que inclua o nome e a idade informada.

nome = input('Olá, qual é o seu nome? ')
idade = input('Agora me diga qual é a sua idade? ')
print('\nOlá {}!\nVejo que você tem {} anos.\nSeja bem-vindo(a)!'.format(nome,idade))