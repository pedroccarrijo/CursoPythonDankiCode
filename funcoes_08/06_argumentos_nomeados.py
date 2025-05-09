#Argumentos nomeados 
#com os argumentos nomedos podemos passalos como parametros na ordem desejada 
#mesmo que o PARÂMETRO NOME foi o primeiro, se nomearmos dentro dos argumentos podemos passalo em qualquer posição
#o nome do parametro deve ser o mesmo nomeado no argumeto (nome, ...) -> (nome="pedro", ...)

def imprimir_nome(nome, sobrenome, idade):
    print(f"nome: {nome}")
    print(f"sobrenome: {sobrenome}")
    print(f"idade: {idade}")

imprimir_nome(sobrenome= "carvalho", idade= 19, nome= "pedro")
