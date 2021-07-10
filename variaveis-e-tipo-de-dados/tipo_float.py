"""
Tipo Float

Tipo real, decimal

Casas decimais.

OBS: O separador de casas decimais na programção é o ponto e não a virgula

"""
# valor = 1,23 -> errado. Aqui gera uma tupla

valor = 1.23  # -> correto
print(valor)
print(type(valor))

#  É possivel fazer dupla atribuição
print('------')
valor1, valor2 = 1, 23
print(valor1)
print(valor2)

# Ao converter valores float para inteiros, perdemos precisão
print('------')
res = int(valor)
print(valor)
print(res)
print(type(res))

#


