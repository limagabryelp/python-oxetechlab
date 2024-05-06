# Execício de Fixação
# Escreva um programa em Python que solicite ao usuário a largura e a altura de um retêngulo. Em seguida, calcula e exiba a área e o perímetro desse retângulo.

a = float(input('Insira a altura do retângulo em m²: '))
l = float(input('Insira a largura do retângulo em m²: '))

# área = altura x largura
# perímetro = 2*(altura + largura)

area = a*l
perimetro = 2*(a + l)

print('O retângulo tem área de {} m² e perímetro de {} m.'.format(area,perimetro))