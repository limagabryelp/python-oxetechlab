# Projeto 1
# Gerenciador de tarefas simples
# Tem que ser possível: adicionar, exibir, remover tarefas, armazenar tarefas, permitir a interação contínua.

resposta_01= str(input('Deseja inserir tarefa (S/N): '))
tarefa = []

while resposta_01 == 'S':
    tarefa.append(str(input('Insira uma tarefa: ')))
    resposta= str(input('Deseja inserir outra tarefa (S/N): '))
    if resposta == 'S':
        tarefa.append(str(input('Insira uma tarefa:')))
        resposta_01 = str(input('Deseja inserir outra tarefa (S/N): '))

print(f'A lista de tarefas {tarefa}')

resposta_02 = str(input('Deseja remover alguma tarefa (S/N): '))

while resposta_02 == 'S':
    tarefa.append(str(input('Insira uma tarefa: ')))
    resposta= str(input('Deseja inserir outra tarefa (S/N): '))
    if resposta == 'S':
        tarefa.append(str(input('Insira uma tarefa:')))
        resposta_01 = str(input('Deseja inserir outra tarefa (S/N): '))

print(f'A lista de tarefas {tarefa}')

tarefa.remove(4)