"""
 - Map

 - Com o map, fazemos mapaamento de valores para função
 - O Map é uma função que recebe dois paramentros: o 1º a função e o 2º um iterável
"""

import math


def area(r):
    """Calcula a área de um circulo com raio"""
    return math.pi * (r ** 2)


# print(area(2))
raios = [2, 5, 7.1, 3, 10, 44]

# forma comun
# areas = []
# for r in raios:
#     areas.append(area(r))
#
# print(areas)

# Usando o Map -

# areas = map(area, raios)
# print(list(areas))


