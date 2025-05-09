#index      0        1        2 
lista = ["carro", "barco", "avião"]
print(lista)

#  for i in lista:
#     print(i)
# print(len(lista))

# for i in range(len(lista)):
#     print(i, lista[i]) 
""" list() """

print("\nlist( ):")
texto = "carro, avião, barco"
lista2 = list(texto)
print(lista2)
#cada caracter é uma casa dentro da lista

""" split() """

print("\nsplit( ):")
texto = texto.split(',')
print(texto)
# split() - separa os elementos nos itens desejados(digitados entre os parenteses)

texto = "carro, avião, barco"
texto = texto.split(',', 1)
print(texto)
# o valor colocado na frente do primeiro parametro indica quantos dos itens ele vai encerar a separação

texto = "pedroccarrijo@gmail.com"
texto = texto.split('@')
print(texto)

""" append() """

print("\nappend( ):")
lista.append("moto")
print(lista)
#append() -> adiciona 1 elemento por vez a lista/vetor, sempre adiciona ao final

""" insert() """

print("\ninsert( ):")
lista.insert(0, 'bicicleta')
print(lista)
#insert() -> adiciona elemento a lista porem na posição escolhida pelo usuario
#primeiro parametro = posição, segundo parametro = adição desejada

""" extend"""

print("\nextend([]):")
lista.extend(["trenó", "fusca"])
print(lista)
#extend([]) -> adiciona mais de 1 elemento a lista/vetor