nome = 'Curso Python'
valor = range(10)

print(nome)
print(valor)

""" list() """
# list() -> separa os itens desejados e atribui/transforma em lista/vetor

print("\nlist( ):")
lista01 = list(range(10)) # ou lista01 = list(valor)
print(lista01)
#pega o selementos presentes no range(10), (0 a 9), e tranforma em uma lista 

lista02 = list("Curso Python"), # ou lista02 = list(nome)
print(lista02)
#pega a str "Curso Python" e separa cada um em casas dentro da lista/vetor

elemento = 8

if elemento in lista01:
    print('8 está dentro')