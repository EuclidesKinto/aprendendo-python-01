"""
Dictionary Comprehension

    - Sintaxe
    {chave:valor for valor in iterável}

"""

# numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#
# quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
# print(quadrado)

numeros = [1, 2, 3, 4, 5, 77, 58, 48, 13]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)