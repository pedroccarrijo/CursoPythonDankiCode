import os

print(os.name) #mostra o sistema operacional 

# Verificar se um arquivo existe
print(os.path.exists('texto.py')) #true or false - para identificar se existe um arquivo com o nome descrito

# Verificar se um diretório existe
print(os.path.exists('manipulacao_de_arquivos_10'))

# Verificar se um arquivo existe dentro de um diretório 
print(os.path.exists('manipulacao_de_arquivos_10/teste.txt'))

# Criando arquivos (não funciona no windows)
# os.mknod('olamundo.py')

# Criando diretório 
#os.mkdir('./manipulacao_de_arquivos_10/testeMkdir.py')

# Apagando arquivos 
#os.remove('manipulacao_de_arquivos_10/teste.txt') # exclusivo para arquivos 
#os.rmdir('manipulacao_de_arquivos_10/testeMkdir.py') # exclusivo para diretótio (pastas)

# Renomear (tbm pode ser alterado o tipo de arquivo)
os.rename("manipulacao_de_arquivos_10/teste.txt", "manipulacao_de_arquivos_10/testeRename.txt")