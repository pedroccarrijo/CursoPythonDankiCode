""" 
Módulos -> arquivos com extensão .py - ou seja - arquivos python
Pacotes -> diretórios contendo conjunto de módulos - pastas com vários arquivos python 
"""

# importação de módulo -> puxar a função de outro arquivo para o desejado
import primo_modulo
print(primo_modulo.primo(6))
print(30*'-')
#primeiro o nome do arquivo e depois o nome da função desejada 

# importa todas as funções do módulo random (ou do modulo desejado) 'utiliza memória sem necessidade'
import random
print(random.random())
print(30*'-')

# importa apenas a função desejada dentro do módulo 'ñ utiliza tanta memória'
from random import random
print(random())
print(30*'-')

# importa mais de uma função do módulo
from random import (
    random, 
    choice
)
print(random())
lista = ["pedra", "papel", "tesoura"]
print(choice(lista)) #sortea um item aleatório 
print(30*'-')

# transformar o nome da função
from random import (
    random as rd
)
print(rd())
print(30*'-')
# (as) passa um outro nome para a utilização da função

# * -> também serve para importar todas as funçoes do módulo 
from random import *
print(randint(1,5))
print(30*'-')

""" dentro de uma outra pasta """
from pacote import principal, secundario
print(principal.soma(2, 3))
print(secundario.quadratica(5))
print(30*'-')

# sub
from pacote.sub import outro 
print(outro.cubica(3))
print(30*'-')

""" se referencia ao nome do módulo """
from  pacote.principal import soma
print(soma(3, 7)) 
print(30*'-')

# sub
from pacote.sub.outro import cubica 
print(cubica(2))