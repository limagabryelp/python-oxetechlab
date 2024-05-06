# Execício de Fixação
# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expresssa em porcentagem e custo, que é o custo de um item antes do imposto. A função "altera" o valor do custo para incluir o imposto sobre vendas.

def somaImposto(custo, taxaImposto):
    somaImposto = custo*(1 + (taxaImposto/100))
    return somaImposto


produto = float(input('Insira o valor do produto: '))
taxa = float(input('Insira o valor da taxa: '))

resultado_somaImposto = somaImposto(produto, taxa)

print(f'O valor final do produto é {resultado_somaImposto}!')