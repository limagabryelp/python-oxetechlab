# Execício de Fixação
# Escreva um programa em Python que solicite ao usuário uma lista de números inteiros. Em seguida, verifique se a lista está vazia. Se estiver vazia, exiba uma mensagem informando. Caso contrário, verifique se a lista possui algum número repetido e exiba uma mensagem adequada.


int_list = input('Digite uma lista de números inteiros separados por uma vírgula: ').split(',')

for i in range(len(int_list)):
    for j in range(i + 1, len(int_list)):
        if int_list[i] == int_list[j]:
            print(f'Existem números iguais na lista: {int_list[i]}.')
            break
    else:
        continue
    break
else:
    print('Não existem números iguais na lista.', int_list)