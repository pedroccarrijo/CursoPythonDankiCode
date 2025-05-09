lista = [1, 2, 3, 4, 5]
print(lista[0])
# item numero 0 = '1'

print(lista[-1])
#contagem inicida pelo final da lista -1 = '5'

print(f'lista[::] -> {lista[::]}')
#imprime todos os itens, o mesmo q -> print(lista)

print(f'lista[1:] -> {lista[1:]}')
# : da continuidade na escrita (começa no termo desejado e continua até p final)

print(f'lista[:3] -> {lista[:3]}')
# a escrita invertida imprime do primeiro item até o desejado (-1)

print(f"lista[1:4] -> {lista[1:4]}")
# imprime entre o intervalo desejado (-1)

print(f'lista[0:5:1] -> {lista[0:5:1]}'), print(f'lista[0:5:2] -> {lista[0:5:2]}')
# ultimo elemento diz quantos elementos vão ser avançados por vez
