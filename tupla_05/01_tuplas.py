lista = ['item1', 'item2', 'item3']
print(lista)
print(len(lista))
print(type(lista))

print('------'*10)

""" tuplas """
#tuplas -> possuem valores imutáveis (os valores atribuidos a variavel não podem ser removidos, adicionados ou alterados)
tupla = ('item1', 'item2', 'item3', 'item1', 'item1')
#tupla = 'item1', 'item2', 'item3', 'item1', 'item1' -> tbm pode ser escrita sem parênteses
print(tupla)
print(len(tupla))
print(type(tupla))

""" count( ) """
print("\ncount( ):")
print(tupla.count('item1'))
# count() -> faz a contagem de quantos elementos tem do parametro desejado 

""" tuple """
print("\ntuple( ):")
tupla = tuple(lista)
print(tupla)
# tuple() -> tranforma a variavel em uma tupla

""" empacotar """
print('\nempacotar:')
tupla = ('item1', 'item2', 'item3')
(x, y, z) = tupla
#cada variavel fica com um elemento, seja ele tupla ou lista (caso seja passado a mesma quantidade de variaveis e a mesma quantidade de elementos da tupla/lista)
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')

#caso a quantidade de variaveis seja menor que a quantidade de elementos, é usado o '*' para que os demais elementos fique juntos na variavel
print("\n")
(x, *y) = tupla
print(f'x = {x}')
print(f'y = {y}')

# o '*' indica onde ficara os elementos "sem variaveis"
tupla = ('item1', 'item2', 'item3', 'item4', 'item5')
print("\n")
(x, *y, z) = tupla
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')