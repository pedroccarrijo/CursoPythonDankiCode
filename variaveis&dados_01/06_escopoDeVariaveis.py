"""
as variaveis globais 
e
as variaveis locais 

"""

x = 5 #global 

def funcao():
    x = 3 #local (apenas dentro da função)
    print(f'Valor da variavel local: {x}')
funcao()

print(f'Valor da variavel global: {x}')

a = 'Pedro' #nome
b = 1.70 #altura
c = '426.380.988.25' #cpf
d = 19 #idade

nome = 'Pedro' 
altura = 1.70 
cpf = '426.380.988.25' 
idade = 19