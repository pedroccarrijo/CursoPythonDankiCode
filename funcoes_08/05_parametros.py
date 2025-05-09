# Parâmetros de uma função 


def nome_da_funcao(parametro): #parâmetro é o nome dado aos valores utilizados na definição de uma função
    #corpo da função 
    print(parametro)

nome = input("Qual o seu nome? ")
nome_da_funcao(nome) # argumento é o nome dado aos valores utilizados na chamada de uma função 

# O(s) PARÂMETRO(s) definido na função é o ARGUMENTO passado no momento em que chamamos a função, todos de forma sequencial
# a quantidade de ARGUMENTOS sempre deve ser a mesma de PARÂMETROS 

def imprime_nome(nome):
    print("Olá, ", nome)

nome = input("Quaol seu nome? ")
imprime_nome(nome)
