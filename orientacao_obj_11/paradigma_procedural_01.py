"""
Paradigma Imperativo - Fortran - Sequência, Decisão e a Iteração
Paradigma Estruturado - C - structs
Paradigma Procedural - Python 
"""
# criando varias variaveis pra cada cadastro de paciente diferente 
nome = "Maria"
idade = 56
cpf = '000.000.000-00'
email = 'maria@gmail.com'

# criando uma matriz para guardar todos os pacientes sem ficar criando varias variaveis 
def Registrar(nome, idade, cpf, email):
    paciente = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'email': email
    }; return paciente

''' terminal '''
# from orientacao_obj_11.paradigma_procedural_01 import Registrar
# paciente = Registrar('Maria Antonieta', 56, '123.456.789-10', 'maria@gmail.com')
# >>> paciente['nome']
# 'Maria Antonieta'
# >>> paciente['idade']
# 56
# >>> paciente['cpf']
# '123.456.789-10'
# >>> paciente['email']
# 'maria@gmail.com'



""" 
Classe - Um conjunto de objetos com as mesmas características 
Objeto - Representação do mundo real como um tipo de dado de uma classe 
Construtor - É uma função criada implicitamente com o mesmo nome da classe 
Atributo - São as variáveis de uma classe
"""

class Paciente: 
    # pass - mesmo a classe vazia não ocorrerá erro
    def __init__(self, nome, idade, cpf, email): #faz referência aos atributos da classe atual (mesmo que o "this" do java, JS )
        print("Acessei o construtor")
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        # >>> paciente = Paciente('Maria', 19, '000.000.000-00', 'maria@gmail.com')
        # Acessei o construtor
        # >>> paciente.nome
        # 'Maria'
        # >>> paciente.cpf
        # '000.000.000-00'
        # >>> paciente.idade
        # 19
        # >>> paciente.email
        # 'maria@gmail.com'

""" 
Simulação de Eventos Discretos -> Paradigma Orientado à Objetos 
Relação -> Destacando as funções e variáveis 

---------------------------------------------------------------

Conceitos Estruturais

-Classe 

Classe é uma estrutura que abstrai um conjunto de objetos com características 
similares. Definindo o comportamento dos seus objetos  através 
das estruturas 

1- Atributos 
2- Métodos 

A classe define um tipo de dado abstrato 


-----------------------------------------------------------------

Conceitos Funadamentais

-Abstração 

Processo pelo qual se isolam aatributos de um objeto, 
considerando os que certo grupos de objetos tenham em comum.

-Reúso

Não existe pior prática em programação do que repetir código

"""
