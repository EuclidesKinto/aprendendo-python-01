"""
List Comprehension

- Utilizando List Comprehension nóes podemos gerar novas listas com dados precessados a partir de outro iterével.

# Sintaxe da List Comprehension
[dado for dado in iterável]
"""

# Exemplo

# numeros = [1, 2, 3, 4, 5, 6]
#
# res = [numero * numero for numero in numeros]
#
# print(res)

numeros = [1, 2, 3, 4, 5, 6]

res = [numero * 2 if numero % 2 == 0 else numero * 10 for numero in numeros]

print(res)

