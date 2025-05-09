""" Método abrindo e fechando arquivo """
print("\nMétodo abrindo e fechando arquivo manual")

arquivo = open('manipulacao_de_arquivos_10/testeLeitura.txt') # atribui e abre o arquivo
print(arquivo.closed) # .closed - retorna se o arquivo está aberto ou não (false = aberto, True = fechado)
print(arquivo.read()) # mostra o conteúdo do todo o arquivo

print(arquivo.readline()) # mostra o conteúdo de uma liha do arquivo (ou você pode passar a quantidade de caracteres a serem exibidos "valor dentro dos parenteses" )

arquivo.close() #fecha o aquivo 
print(arquivo.closed)


""" Método abrindo e fechando arquivo automático"""
print("\nMétodo abrindo e fechando arquivo automático")

with open('manipulacao_de_arquivos_10/testeLeitura.txt') as x: #valor passado após o "as" é o nome que será usado para o arquivo aberto 
    print(x.read())