"""
Lambdas

    - Conhecidas por Expressões Lambdas ou simplesmente Lambdas, são funções sem nome, ou seja, funções anônimas
    - Podemos ter expressões lambdas com múltiplas entradas
"""


# calc = lambda x: 3 * x + 1
# print(calc(5))

# full_name = lambda first_name, last_name: first_name.strip().title() + ' ' + last_name.strip().title()
#
# print(full_name('  MariO', 'SILVA     '))

# Ordenando por Sobrenome
nomes = ['Euclides Quinto', 'Ferdinand Sousa', 'Tobias Cazer', 'Eike Doval', 'Joaquim Welder']
nomes.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(nomes)
