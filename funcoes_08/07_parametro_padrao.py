#Parâmetro padrão 
#O parâmetro padrão serve para que quando não for passado um argumento a função tenha uma resposta como padrão e noa gere erro
#Argumentos OBRIGATÓRIOs são o que não possui valor padrão e é necessario um valor para a função funcionar 
#Argumentos NÂO OBRIGATÓRIOs são os que ja possuem um valor por padrão
# Os argumentos Não Obrigatórios devem vir depois dos Obrigatórios na passagem dos parâmetros 

# foram definidos palavras expecificas caso não seja passado arfumentos 
def imprimir_nome(nome="nome", sobrenome="sobrenome", idade="idade"):
    print(f"nome: {nome}")
    print(f"sobrenome: {sobrenome}")
    print(f"idade: {idade}")
    print("--------------------------")

imprimir_nome()
imprimir_nome(sobrenome= "carvalho", idade= 19, nome= "pedro")


# None é um espaço vazio - sem valor 
def imprimir_nome(nome= None, sobrenome= None, idade= None):
    print(f"nome: {nome}")
    print(f"sobrenome: {sobrenome}")
    print(f"idade: {idade}")
    print("--------------------------")

imprimir_nome()
imprimir_nome(sobrenome= "carvalho", idade= 19, nome= "pedro")


# None é um espaço vazio - sem valor (caso não tenha valor as mensagens serão diferentes de quando estiverem com)
def imprimir_nome(nome= None, sobrenome= None, idade= None):
    if nome != None:
        print(f"nome: {nome}")
        print(f"sobrenome: {sobrenome}")
        print(f"idade: {idade}")
        print("--------------------------")
    else:
        print("Por favot insira seus dados: ")
        print("--------------------------")

imprimir_nome()
imprimir_nome(sobrenome= "carvalho", idade= 19, nome= "pedro")


#Exemplo de número de argumentos <= a número de parâmetros
def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
    print("--------------------------")
    print(f"Título: {nomeImovel}")
    print(f"Quartos: {n_quartos}")
    if vagasGaragem != None:
        print(f"Vagas de garagem: {vagasGaragem}")

imprimir_imovel("Casa 3 quartos - SP", 3)
imprimir_imovel("Apartamento - MG", 2, 1)

# Exemplos de números de argumentos > números de parâmetros 
imprimir_imovel("Loja Comercial", 2, 0, "desconto")

