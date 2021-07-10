"""
Recebendo dados do usuário

input() -> td dados recebido via input() é do tipo String -> str

Em Python, string é tudo que estiver entre: aspas simples; aspas duplas; aspas simples triplas e aspas duplas triplas.
    Ex: - 'Euclides'
        - "Euclides"
        - '''Euclides'''
"""
# Entrada de dados
# print("Qual é o seu nome?")
# nome = input()  # Input -> Entrada

nome = input("Qual é o seu nome?")

# saída de dados
# Exemplo de print 'antigo' 2.x do python
# print("Seja bem-vindo(a) %s " % nome)
# print("Seja bem-vindo(a)".format(nome))
print(f"Seja bem-vindo(a) {nome}")

# print('Qual a sua idade?')
# idade = input()
idade = int(input("Qual é a sua idade?"))


# print('A {0} tem {1} anos'.format(nome, idade))
print(f'A {nome} tem {idade} anos')

"""
int(idade) => cast

Cast é a conversão de um tipo de dao para outro

"""
# print(f'O {nome} nasceu em {2021 - int(idade)}')

print(f'O {nome} nasceu em {2021 - idade}')
