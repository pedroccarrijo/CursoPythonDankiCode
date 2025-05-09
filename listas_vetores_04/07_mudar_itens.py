lista = ['gato', 'cachorro', 'peixe', 'cavalo', 'tubarão', 'girafa']
print(lista)

lista[1] = 'cavalo'
print(lista)

lista[1:4] = ['águia', 'morcego', 'elefante']
print(lista)

lista[1:3] = ['macaco', 'porco', 'leão'] # alterado mais elementos do que o passado na variavel -> lista[1:3] -> = 2 casas dentro da lista, 1 e 2 
print(lista)
# ao invez de ignorar o item a+, ele é adicionado a proxima casa da lista (aumentado o seu tamanho)
