# Argumento Arbitrário **Kwargs - Keyword Arguments 
# Essa função recebe argumentos que serão atribuídos em um dicionário

def imprimir_nomes(**nomes):
    print(nomes)

imprimir_nomes(nomes="ana", sobrenomes="silva")

# **kwargs ->  não necessariamente precisa ser escreto "**kwargs", pode ser usaddo qualquer nome desde que esteja com os asteriscos '**'
# é utilizado quando não se sabe ao certo quantos ARGUMENTOS NOMEADOS uma função vai receber - { 'nome': "pedro" }
