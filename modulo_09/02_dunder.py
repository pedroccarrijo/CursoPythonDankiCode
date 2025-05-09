""" 
Objetos Dunder
Dunder - Duplo Underscore - Duplo Underline __ 
Atributos Mágicos - variáveis 
Métodos Mágicos - funções

__init__ -> 
__name__ -> ver o nome do arquivo
__main__
__file__ -> mostra o caminho onde o arquivo se encontra salvo
__doc__ - Docstrings ( mostra oque esta dentro das aspas triplas  """ """aqui""" """ )

help("nome do modulo") -> mostra NOME (nome e oque compõe o modulo), FUNCTIONS (nome das funções dentro do módulo quais parametros são passados para cada uma)

"""
# import 03_dunder
# 03_dunder.__ (função desejada) __

#execução "parcial" do arquivo
import primo_modulo
print(primo_modulo.primo(7)) # restante no arquivo (primo_modulo.py) 

import random