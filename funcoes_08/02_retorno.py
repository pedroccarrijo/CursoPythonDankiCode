""" lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
print(lista)
print(f"retorno da função pop(): {retorno}") """

# Usando return em funções 

def ola_mundo():
    print("ola mundo")

ola_mundo()

def par_impar():
    num = 3
    if num % 2 == 0:
        return "Número par"
    else: return "Número impar"

print(par_impar())

# Assim que o interpretador ler o primeiro return ele sai da função  (todo o restante da função é interrompido)
#se a função retorna uma frase porem sem a função print, a função deve ser chamada dentro de um print