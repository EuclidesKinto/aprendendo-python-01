"""

**kwargs

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos="verde", julia="rosa", thiago="preto", ana="azul")

# OBS: Os parâmetros *args e **kwargs não são obrigatórios

cores_favoritas()
cores_favoritas(kinto="blue")
=========================================
Nas funções, podemos ter nesta ordem:
   1- Parâmetros obrigatórios
   2- *args
   3- Parâmentros DEFAULT (não obrigatórios)
   4- **kwargs

   exemplo:
   def my_function(age, name, *args, solteiro=False, **kwargs):
    print(f'{name} tem {age} anos!')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


my_function(10, 'Ana')
my_function(20, 'Xixo', 4, 5, 2, solteiro=True)
my_function(18, 'Dede', eu='não', voce='sim')
my_function(59, 'Didi', 9, 10, 11, java=False, python=True)


=========================================
"""



