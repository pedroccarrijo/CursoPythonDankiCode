"""
Exercício de troca de variáveis 

"""

# Trocando variáveis em python  

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

# Criamos uma variavel auxiliar

aux = x 
x = y 
y = aux

print(f'O valor de x depois da troca é de: {x}')
print(f'O valor de y depois da troca é de: {y}')
