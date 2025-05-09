#Paradigma imperativo
#imperare -> comandar 

#caracteristicas: variáveis, atribuições e sequência
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2 

#bloco externo
nome = "Gabriel" #variável global 


def minha_funcao():
    #bloco interno ou corpo da função 
    nome = "Pedro" #variável local
    print(nome)
    

print(nome)
minha_funcao() #chamando a função(def)