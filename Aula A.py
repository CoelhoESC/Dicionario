"""
Dicionario
"""
dict_1 = {'chave1': 1, 'chave2': 2, 'chave3': 3}
dict_2 = dict(chave4=4, chave5=5, chave6=6)


print("Adquirindo valor, mudando valor e adicionando valor")
print(dict_1['chave1'])  # Adquirindo
dict_1['chave2'] = 20  # Mudando
dict_1.update({'Chave4': 10}) # adicionando
print(dict_1)

print('\nA chave (key) pode ser qualquer tipo de valor')
dict_3 = {'str': 'Everton', 123: 123, (1, 2, 3, 4): 'Tupla'}
print(dict_3[(1, 2, 3, 4)])

print('\nPode fazer verificações')
print(dict_1.get('Nome_da_chave'))  # Verificando se existe essa chave no dicionario - retorna NONE
print('chave1' in dict_1)  # Retorna valores boolean True/ False
print(1 in dict_1.values())

print('\nExcluindo chaves')
del dict_2['chave4']
dict_2.pop('chave5')
dict_2.popitem()  # Exclui o ultimo numero!

print('Iteragindo com dict ( keys, values e items')
print()
for k in dict_1.keys():
    print(k)
print()
for v in dict_1.values():
    print(v)
print()
for t in dict_1.items():
    print(t)  # Retorna uma tupla
    print(t[0], t[1])
print()
for k, v in dict_1.items():
    print(k, v)
print()

print('Convertendo um dict para list')
Lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
]
dict_4 = dict(Lista)  # Pode ser fazer test cast! Mas tem que similar a um Dicionario!
print(dict_4)         # Lista dentro de tupla! Tupla dentro de lista! Tupla com tupla!


print('\nPode fazer uma concatenação')
dict_1.update(dict_3)
print(dict_1)
