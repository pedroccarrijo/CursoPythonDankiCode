""" 
listas: Colelção ordenada, mutável e que permite valores duplicados -> (list)
Tuplas: Coleção ordenada, imutável e que permite valores duplicados -> (tuple)
Dicionários: Coleção não oredenada, mutável e que não permite valores duplicados -> (dict)

"""
#index     0         1        2
lista = ["item1", "item2", "item3"]
#index     0         1        2
tupla = ("item1", "item2", "item3")

#chave: valor
dicionario = {
    "nome": "Pedro", 
    "idade": 19, 
    "cidade": "Franca"
    }
print(dicionario)
print(type(dicionario))
# tbm escrito -> x = {'nome': 'Pedro', 'idade': 19, 'cidade': 'Franca'}
#as chaves não podem se repetir, caso aconteça ele usara o ultimo valor recebido

print(dicionario["nome"])
#é chamado pelo nome da chave e não por valor do index (já que ela não possui)

""" get() """
print("\nget( ):")
print(dicionario.get("idade"))
# get() -> mostra o valor da chave passada como parametro

""" keys() """
print("\nkeys( ):")
print(dicionario.keys())
# keys() -> mostra o nome de todas as chaves presentes no dicionário/variável

""" values() """
print("\nvalues( ):")
print(dicionario.values())
# values() -> (mostra os valores presentes nas chaves

""" items() """
print("\nitems( ):")
print(dicionario.items())
# item() -> mostra todas as chaves e valores 

""" alter valores """
print("\nalterar valores")
dicionario["cidade"] = "Ribeirão Preto"
print(dicionario)

""" update() """
print("\nupdate( ):")
dicionario.update({"cidade":"Franca"})
print(dicionario)
#caso a chave já exista ela é modificada

dicionario.update({"ano":"2005"})
print(dicionario)
#caso a chave não exista ela é adicionada

""" popitem() """
print("\npopitem( ):")
dicionario.popitem()
print(dicionario)
# popitem() -> elimina o último elemento da variável

""" pop() """
print("\npop( ):")
dicionario.pop("idade")
print(dicionario)
# pop() -> elimina um elemento específico

""" del """
print("\ndel( ):")
del dicionario["nome"]
print(dicionario)
# del -> deleta o item

""" clear() """
print("\nclear( ):")
dicionario.clear()
print(dicionario)
#clear() -> limpa a variável

""" dict() """
# copia um dicionario ou tranforma uma variavel em um 
dicionario = {
    "nome": "Pedro", 
    "idade": 19, 
    "cidade": "Franca"
    }
print("\ndict( ):")
dicionario02 = dict(dicionario)
print(dicionario)
print(dicionario02)

print('------'*10)

dicionario["cidade"] = "Ribeirão Preto"
print(dicionario)
print(dicionario02)