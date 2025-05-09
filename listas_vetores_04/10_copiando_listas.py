lista1 = ["a", "b", "c"]
lista2 = [1, 2, 3]

# lista1 = lista1 + lista2
# print(lista1)

# lista1.extend(lista2)
# print(lista1)

""" adição """
print("adição:")
for i in lista2:
    lista1.append(i)
print(lista1)

""" cópia """
print("\ncópia:")

lista1 = ["a", "b", "c"]
lista3 = lista1
print(lista1)
print(lista3)

lista1.append("d")
print(lista1)
print(lista3)

#tudo que é adicionado a lista1 tbm passa para lista3

""" copy( ) """
print("\nusando .copy():")
lista4 = lista1.copy()
print(lista4)

lista1.append("e")
print(lista1)
print(lista4)
#caso sejá adicionado algum item na lista1 após a cópia, não será adicionado a lista cópia 