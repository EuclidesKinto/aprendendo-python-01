"""
Any e All

all() -> retorna True se todos os elementos do iterável são todos verdadeiros ou ainda se o iterável está vazio

"""

#  Exemplo de all()

print(all([0, 1, 2, 3]))  # Todos os numeros são vdd? -> False
print(all([1, 2, 3]))  # Todos os numeros são vdd? -> True
print(all([]))  # Todos os numeros são vdd? -> True

nomes = ['Carlos', 'Camila', 'Carla']

print(all([nome[0] == "C" for nome in nomes]))
