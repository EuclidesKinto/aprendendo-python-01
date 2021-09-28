"""
 - Listas Aninhadas
"""

# listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# iterando com loops em uma lista aninhada

# for lista in listas:
#     for num in lista:
#         print(num)

# List Comprehension

# [print(lista) for lista in listas]
#
# [[print(valor) for valor in lista] for lista in listas]
x = 3
tab = [[num for num in range(1, x)] for valor in range(1, x)]
print(tab)
