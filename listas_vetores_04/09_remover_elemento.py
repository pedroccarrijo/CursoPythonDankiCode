lista = ['carro', 'barco', 'avião']
print(lista)

""" pop() """
# pop() -> remove elementos da lista
print("\npop( ):")
lista.pop()
print(lista)
#como não foi passado nenhum paarametro ele remove o ulrimo elemento da lista
lista.pop(0)
print(lista)
#removeu o parametro desejado

""" remove() """
# remove() -> remove elementos da lista - diferente do pop pois não remove pelo index da lista e sim por argumento
print("\nremove( ):")
lista = ['carro', 'barco', 'avião']

lista.remove('barco')
print(lista)

""" del """
# del -> deleta uma variavel ou lista
# também deleta itens dentro da lista 
print("\ndel:")
lista = ['carro', 'barco', 'avião']

del lista[0]
print(lista)
"""
del lista
print(lista) #Erro

"""

""" clear() """
# clear() -> limpa todos os dados dentro da lista

print("\nclear( ):")
carrinho_de_compras = ["pão", "carne", "verduras"]
print(carrinho_de_compras)

carrinho_de_compras.clear()
print(carrinho_de_compras)

""" sort() """
# sort() -> ordena os elementos em ordem alfabetica ou numericas

print("\nsort( ): \npalavras:")
#alfabetica
carrinho_de_compras = ["pão", "carne", "verduras"]
print(carrinho_de_compras)

carrinho_de_compras.sort()
print(carrinho_de_compras)

# numeros
print("\nOrdem numérica:")
lista = [1, 340, 458, 36, 45]
print(lista)
lista.sort()
print(f'crescente: {lista}')
lista.sort(reverse= True)
print(f'decrescente: {lista}')

# alfabetica Mm
print("\nMAIÙSCULA e minúscula:")
lista = ["Ana", "Pedro", "Marta", "Clarice", "beatriz", "ana clara"]
print(lista)

lista.sort()
print(lista)
# primeiro são ordenadas as str com letras maiúsculas e depois as com letras minúsculas 
print("sort(key = str.lower):")
lista.sort(key = str.lower)
print(lista)
# é passado uma chave como parametro para que a função siga
# os elementos dentro da lista não são modificados, apenas remete como se fossem da forma do parametro

""" reverse() """
# reverse() -> reverte a lista
print("\nreverse( ):")
lista = [1, 340, 458, 36, 45]
print(lista)

lista.reverse()
print(lista)

