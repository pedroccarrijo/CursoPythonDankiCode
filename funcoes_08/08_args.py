# o argumento arbitrário *args

def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *args):
    print("--------------------------")
    print(f"Título: {nomeImovel}")
    print(f"Quartos: {n_quartos}")
    if vagasGaragem != None:
        print(f"Vagas de garagem: {vagasGaragem}")

imprimir_imovel("Loja Comercial", 2, 5, "(16) 9 9999-8888")




def imprimir_nomes(*nomes):
    print(nomes)

imprimir_nomes("ana", "beatriz", "pedro", "joão")

# *args -> não necessariamente precisa ser escreto "*args", pode ser usaddo qualquer nome desde que esteja com o asterisco '*'
# é utilizado quando não se sabe ao certo quantos ARGUMENTOS uma função vai receber
# é tranformado em tupla

lista = ["guilherme", "maria", "luiza"]
imprimir_nomes(lista)
# imprime a lista como um unico item dentro de uma tupla

imprimir_nomes(*lista)
# separa os itens da lista e coloca cada um como um item diferente dentro da tupla