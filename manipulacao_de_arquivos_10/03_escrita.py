"""  w  """
with open('manipulacao_de_arquivos_10/testeLeitura.txt', 'w') as arquivo: # 'w' = write, permite sobrescrever dentro do arquivo 
    arquivo.write("Teste Escrita Write 'w'") #sobrescreve o que estava anteriormente

"""  a  """
with open('manipulacao_de_arquivos_10/testeLeitura.txt', 'a') as arquivo: # 'a' = permite adicionar escrita dentro do arquivo 
    arquivo.write("\nTeste de adição de escrita 'a'") #adiciona com o que já existe 

texto = """ Mala
    Camisa
    Calça 
    Meia
    Short
    Chinelo
"""

with open('manipulacao_de_arquivos_10/testeLeitura.txt', 'a') as arquivo:  
    arquivo.write(f'\n {texto}')