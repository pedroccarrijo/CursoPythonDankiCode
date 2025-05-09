""" 
listas: Colelção ordenada, mutável e que permite valores duplicados -> (list)
Tuplas: Coleção ordenada, imutável e que permite valores duplicados -> (tuple)
Dicionários: Coleção não oredenada, mutável e que não permite valores duplicados -> (dict)
Sets: Coleção não ordenada, imutável e que não permite valores duplicados -> (set)

"""

#Os sets tbm são conhecidos como conjuntos

conjunto = {"item1", "item2", "item3"}
print(conjunto)
print(type(conjunto))
#a ordem de impressão é sempre escrita aleatoria, pois é uma coleção não ordenada

conjunto = {"item1", "item2", "item3", "item1", "item2"}
print(conjunto)
print(type(conjunto))
# se houver repetição de elementos ele ignora

""" set() """
#set() -> transforma outras variáveis em sets
print("\nset( ):")
tupla = (3, 7, 9, 5)
conjunto = set(tupla)
print(conjunto)
