"""
Fazendo uma copia do dict
Para se fazer uma copia de dicionarios, precisamos da biblioteca copy. Quando se fazer uma copia, usando .copy() proprio
do dicionario, os dois dicionarios, tanto original e a copia, serão o mesmo. Quando mudar o valor do dicionario copia,
automaticamente tambem irá mudar o dicionario original, pois os ID são os mesmo.
Para isso se isa deepcopy()
"""

import copy

Clientes = {'cliente1': {'nome': 'Everton', 'sobrenome': 'Coelho'},
            'cliente2': {'nome': 'Anna', 'sobrenome': 'Vieria'},
            'cliente3': {'nome': 'Matheus', 'sobrenome': 'Moreira'},
            }
for clientes_k, clientes_v in Clientes.items():  # Iteragir com as primeiras chaves (clienteN)
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():  # Iteragir com as informações dos clientes
        print(f'\t {dados_k} = {dados_v}')

print('\nFazendo copias')
d1 = {1: 2, 2: 3, 3: 4}
v = d1.copy()  # Copia rasa!
C = copy.deepcopy(d1)  # Copia real!

print('\nCopia raza, usando copy() do dicionario')
d2 = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': ['Everton', 'Coelho']}
copia_raza = d2.copy()
copia_raza['key4'][0] = 'Airton'  # trocando valor

print(f'Dicionario Original: {d2}')  # Mesmo sendo uma copia, elas são modificadas juntas
print(f'Dicionario Copia: {copia_raza}')
