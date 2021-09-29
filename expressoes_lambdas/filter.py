"""
 - Filter
 filter() -> Serve para filtrar dados de uma determinada coleção.

"""

# valores = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# media = (sum(valores) / len(valores))
# print(media)

# Biblioteca para trabalhar com dados estatisticos
import statistics

# dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
# print(f'dados: {dados}')
# Calculando a média dos daos utilizando a função mean()
# media = statistics.mean(dados)
# print(f'media: {media}')

# OBS: Assim como a função map(), a filter() recebe dois paramentros, sendo uma função e um iterável

# retornando somente valores acima da média
# res = filter(lambda valor: valor > media, dados)
# print(f'Valores acima da média: {list(res)}')

# users = [
#     {"username": "Dina", "tweets": ['Eu xxxxxxx', 'yyyyyyyyy']},
#     {"username": "Doca", "tweets": ['Eu xxxxxxx']},
#     {"username": "Ena", "tweets": []},
#     {"username": "Jo", "tweets": ['Eu xxxxxxx', 'yyyyyyyyy', 'ooooooo']},
#     {"username": "Rafa", "tweets": []},
# ]

# Filtrar users que estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda user: len(user['tweets']) == 0, users))

# Forma 2
# inativos = list(filter(lambda user: not user['tweets'], users))
# print(inativos)





















